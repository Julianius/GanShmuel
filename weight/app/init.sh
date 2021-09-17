#!bin/bash

export DYNAMIC_PORT=8083

docker-compose up --build



        <a href="{{ url_for('health') }}">
            <i class="fa fa-home"></i> health
        </a>
        <a   href="{{ url_for('batch_weight') }}">
            <i class="fas fa-tools"></i> batch-weight
        </a>
        <a href="{{ url_for('weight') }}">
            <i class="fa fa-home"></i> weight
        </a>
        <a   href="{{ url_for('item') }}" >
            <i class="fas fa-tools"></i>item
        </a>
        <a href="{{ url_for('session') }}">
            <i class="fa fa-home"></i> session
        </a>
        <a   href="{{ url_for('unknown') }}">
            <i class="fas fa-tools"></i> unknown
        </a>