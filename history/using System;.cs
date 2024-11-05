using System;
using System.Threading;
using NModbus;
using NModbus.Serial;
using System.IO.Ports;

class Program
{
    private static int n = 0;
    private static int[] result = { 2, 2 };
    private static IModbusSerialMaster master;
    private static SerialPort port;

    static void Main(string[] args)
    {
        // 初始化串口
        port = new SerialPort("COM1", 115200, Parity.None, 8, StopBits.One);
        port.Open();

        // 创建Modbus主站
        var factory = new ModbusFactory();
        master = factory.CreateRtuMaster(port);

        while (true)
        {
            ReadModbus();
            LightUp();
            InputN();
            ReadModbus();
            Thread.Sleep(500);
            Setup();
            Thread.Sleep(2000);
            ReadModbus();
            n = 0;
            Setup();
            ShutLight();
            port.Close();
        }
    }

    static void InputN()
    {
        try
        {
            Console.Write("Enter 1 to open the door or 0 to close the door: ");
            n = int.Parse(Console.ReadLine());
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input");
        }
    }

    static void LightUp()
    {
        while (result[0] == 1)
        {
            Console.Write("\rputting hand into it");
            Thread.Sleep(1000);
            ReadModbus();
        }
        SendCommand("02 06 00 00 00 01 48 39"); // 手来开
        ReadModbus();
    }

    static void CkLightDown()
    {
        if (result[0] == 1)
        {
            SendCommand("02 06 00 00 00 00 89 F9"); // 手去关
        }
    }

    static void ShutLight()
    {
        SendCommand("02 06 00 00 00 00 89 F9");
    }

    static void ReadModbus()
    {
        ushort address = 0x101;
        ushort count = 1;
        byte slaveId = 1;

        var D = master.ReadHoldingRegisters(slaveId, address, count);
        if (D != null && D.Length > 0)
        {
            int p = D[0];
            if (p == 900)
            {
                Console.WriteLine("The door is open");
                result[1] = 1;
            }
            else if (p == 300)
            {
                Console.Write("\rThe door is closed");
                result[1] = 0;
            }
            else
            {
                Console.WriteLine("The door is in an unknown position");
                result[1] = -1;
            }
        }
        else
        {
            Console.WriteLine("Failed to read registers");
        }

        address = 0x200;
        slaveId = 2;
        var hand = master.ReadHoldingRegisters(slaveId, address, count);
        if (hand != null && hand.Length > 0)
        {
            if (hand[0] == 1)
            {
                Console.Write("\rthere is no hand");
            }
            else
            {
                Console.Write("\rthere is a hand");
            }
            result[0] = hand[0];
        }
        else
        {
            Console.WriteLine("Failed to read registers");
        }
    }

    static void SendCommand(string hexData)
    {
        try
        {
            byte[] data = HexStringToByteArray(hexData);
            master.WriteMultipleRegisters(1, 0, data);
            Console.WriteLine("Command sent");
        }
        catch (Exception err)
        {
            Console.WriteLine($"An error occurred: {err.Message}");
        }
    }

    static byte[] HexStringToByteArray(string hex)
    {
        hex = hex.Replace(" ", "");
        byte[] bytes = new byte[hex.Length / 2];
        for (int i = 0; i < bytes.Length; i++)
        {
            bytes[i] = Convert.ToByte(hex.Substring(i * 2, 2), 16);
        }
        return bytes;
    }

    static void Setup()
    {
        if (result[0] == 1)
        {
            if (result[1] == 0 && n == 1)
            {
                SendCommand("01 06 00 80 03 84 88 B1");
                Console.WriteLine("Door is opening");
            }
            else if (result[1] == 1 && n == 0)
            {
                SendCommand("01 06 00 80 01 2C 88 6F");
                Console.WriteLine("Door is closing");
            }
            else
            {
                if (n == 1 || n == 0)
                {
                    Console.WriteLine("Door is already in the desired position");
                    Console.WriteLine($"n = {n}, door = {result[1]}");
                }
                else
                {
                    Console.WriteLine("Invalid setup input");
                }
            }
        }
        else
        {
            Console.Write("\r Please remove the hand before setting up the door");
        }
    }
}
