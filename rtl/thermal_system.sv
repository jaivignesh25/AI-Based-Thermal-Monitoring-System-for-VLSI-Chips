`timescale 1ns / 1ps

module thermal_system (

    input logic              clk,
    input logic              rst,
    input logic signed [8:0] sensor1_step,
    input logic signed [8:0] sensor2_step,
    input logic signed [8:0] sensor3_step,
    output logic              alert,
    output logic [1:0]        thermal_status,
    output logic signed [8:0] temp_change,
    output logic [1:0]        change,
    output logic              trend_valid
);

    logic [7:0] temp1;
    logic [7:0] temp2;
    logic [7:0] temp3;
    logic [7:0] zone1;
    logic [7:0] zone2;
    logic [7:0] zone3;
    thermal_monitor monitor (

        .clk          (clk),
        .rst          (rst),
        .sensor1_step (sensor1_step),
        .sensor2_step (sensor2_step),
        .sensor3_step (sensor3_step),
        .temp1        (temp1),
        .temp2        (temp2),
        .temp3        (temp3)

    );

    data_aggregator aggregator (

        .clk   (clk),
        .rst   (rst),
        .temp1 (temp1),
        .temp2 (temp2),
        .temp3 (temp3),
        .zone1 (zone1),
        .zone2 (zone2),
        .zone3 (zone3)

    );

    hotspot_detector detector (

        .clk   (clk),
        .rst   (rst),
        .zone1 (zone1),
        .zone2 (zone2),
        .zone3 (zone3),
        .alert (alert)

    );

    thermal_severity severity (
        .zone1          (zone1),
        .zone2          (zone2),
        .zone3          (zone3),
        .thermal_status (thermal_status)
    );

    trend_detector trend (

        .clk          (clk),
        .rst          (rst),
        .current_temp (zone3),
        .temp_change  (temp_change),
        .change       (change),
        .trend_valid  (trend_valid)
    );

endmodule