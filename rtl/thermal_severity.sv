`timescale 1ns / 1ps

module thermal_severity #(    parameter normal   = 2'b00,
    parameter warning  = 2'b01,
    parameter critical = 2'b10
)(
input logic [7:0] zone1,
input logic [7:0] zone2,
input logic [7:0] zone3,
output logic [1:0]thermal_status

    );

    
    always_comb begin 
    if ((zone1>8'd75) || (zone2>8'd75) || (zone3>8'd75)) begin
    thermal_status = critical;
    end
    else if ((zone1>8'd60) || (zone2>8'd60) || (zone3>8'd60)) begin
    thermal_status = warning;
    end
    else begin 
    thermal_status = normal;
    end
    end
    
endmodule
