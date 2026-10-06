`timescale 1ns / 1ps

module hotspot_detector (
    input  logic       clk,
    input  logic       rst,
    input  logic [7:0] zone1,
    input  logic [7:0] zone2,
    input  logic [7:0] zone3,
    output logic       alert
);

    always_comb begin

        if (rst)
            alert = 1'b0;

        else if ((zone1 > 8'd75) ||
                 (zone2 > 8'd75) ||
                 (zone3 > 8'd75))
            alert = 1'b1;

        else
            alert = 1'b0;

    end

endmodule