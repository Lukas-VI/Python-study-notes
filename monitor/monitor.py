import psutil
from flask import Flask, jsonify, render_template
import time as t
import os

from zmq import device

app = Flask(__name__)

class Monitor:
    #通过os模块获取系统信息设备型号
    device_id = os.popen('wmic csproduct get uuid').read().split('\n')[1].strip()
    #通过psutil模块获取系统信息
    system_info = {
        'device': device_id,
        'cpu_count': psutil.cpu_count(),
        'cpu_freq': psutil.cpu_freq().max,
        'memory': psutil.virtual_memory().total,
        'disk': psutil.disk_usage('/').total
    }

    def get_resources():
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent

        return jsonify({
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_usage': disk_usage,
        })


    
    def print_system_resources():
        #遍历字典，打印系统信息
        for key, value in Monitor.system_info.items():
            print(key, ':', value,"\n")


@app.route('/')
def index():
    Monitor.print_system_resources()
    return render_template('portal.html')

@app.route('/api/resources')


if __name__ == '__main__':
    app.run(debug=True)
