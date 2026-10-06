`timescale 1ns / 1ps

module thermal_monitor (

    input logic              clk,
    input logic              rst,

    input logic signed [8:0] sensor1_step,
    input logic signed [8:0] sensor2_step,
    input logic signed [8:0] sensor3_step,

    output logic [7:0]       temp1,
    output logic [7:0]       temp2,
    output logic [7:0]       temp3
);

    temp_sensor #(
        .INITIAL_TEMP(25)
    ) sensor1 (

        .clk      (clk),
        .rst      (rst),
        .temp_step(sensor1_step),
        .temp_out (temp1)

    );

    temp_sensor #(
        .INITIAL_TEMP(35)
    ) sensor2 (

        .clk      (clk),
        .rst      (rst),
        .temp_step(sensor2_step),
        .temp_out (temp2)

    );

    temp_sensor #(
        .INITIAL_TEMP(45)
    ) sensor3 (

        .clk      (clk),
        .rst      (rst),
        .temp_step(sensor3_step),
        .temp_out (temp3)

    );

endmodule