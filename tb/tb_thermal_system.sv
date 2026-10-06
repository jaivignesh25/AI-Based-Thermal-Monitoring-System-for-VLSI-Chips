`timescale 1ns / 1ps

module tb_thermal_system;

    logic clk;
    logic rst;
    logic signed [8:0] sensor1_step;
    logic signed [8:0] sensor2_step;
    logic signed [8:0] sensor3_step;
    logic alert;
    logic [1:0] thermal_status;
    logic signed [8:0] temp_change;
    logic [1:0] change;
    logic trend_valid;
    logic [7:0] temp1;
    logic [7:0] temp2;
    logic [7:0] temp3;
    logic [7:0] zone1;
    logic [7:0] zone2;
    logic [7:0] zone3;
    integer file;

    logic first_sample;

    thermal_system dut (
        .clk(clk),
        .rst(rst),
        .sensor1_step(sensor1_step),
        .sensor2_step(sensor2_step),
        .sensor3_step(sensor3_step),
        .alert(alert),
        .thermal_status(thermal_status),
        .temp_change(temp_change),
        .change(change),
        .trend_valid(trend_valid)
    );
    assign temp1 = dut.temp1;
    assign temp2 = dut.temp2;
    assign temp3 = dut.temp3;
    assign zone1 = dut.zone1;
    assign zone2 = dut.zone2;
    assign zone3 = dut.zone3;


    initial begin
        clk = 1'b0;
        forever begin
            #20ns;
            clk = ~clk;
        end
    end
    initial begin
        rst = 1'b1;
        sensor1_step = 9'sd0;
        sensor2_step = 9'sd0;
        sensor3_step = 9'sd0;
        file = 0;
        first_sample = 1'b1;
    end

    initial begin
        file = $fopen(
            "E:/VLSI projects/AI-Based Thermal Monitoring System/ML/realtime_thermal.csv",
            "w"
        );

        if (file == 0) begin

            $display("ERROR: Cannot open realtime_thermal.csv");

        end
        else begin

            $fwrite(
                file,
                "time,temp1,temp2,temp3,zone1,zone2,zone3,alert,status,temp_change,trend,trend_valid\n"
            );

            $fflush(file);
        end
    end

    initial begin

        wait(file != 0);

        forever begin

            @(posedge clk);

            #1ns;

            if (!rst && trend_valid) begin
                if (first_sample) begin

                    first_sample = 1'b0;

                end
                else begin
                    $display(
                        "Time=%0t | rst=%0b | temp1=%0d temp2=%0d temp3=%0d | zone1=%0d zone2=%0d zone3=%0d | ALERT=%0b | STATUS=%02b | CHANGE=%0d | TREND=%02b",
                        $time,
                        rst,

                        temp1,
                        temp2,
                        temp3,

                        zone1,
                        zone2,
                        zone3,

                        alert,
                        thermal_status,
                        temp_change,
                        change
                    );


                    $fwrite(
                        file,
                        "%0t,%0d,%0d,%0d,%0d,%0d,%0d,%0b,%0d,%0d,%0d,%0b\n",

                        $time,

                        temp1,
                        temp2,
                        temp3,

                        zone1,
                        zone2,
                        zone3,

                        alert,
                        thermal_status,

                        temp_change,
                        change,
                        trend_valid
                    );

                    $fflush(file);

                end

            end

        end

    end

    initial begin
        #40ns;
        rst = 1'b0;
        sensor1_step = 9'sd1;
        sensor2_step = 9'sd0;
        sensor3_step = 9'sd2;

        #600ns;

        sensor1_step = 9'sd1;
        sensor2_step = 9'sd2;
        sensor3_step = 9'sd3;

        #600ns;
        sensor1_step = 9'sd0;
        sensor2_step = 9'sd2;
        sensor3_step = 9'sd0;

        #400ns;

        sensor1_step = -9'sd1;
        sensor2_step = -9'sd2;
        sensor3_step = -9'sd2;

        #600ns;
        sensor1_step = 9'sd2;
        sensor2_step = -9'sd1;
        sensor3_step = 9'sd3;

        #600ns;
        sensor1_step = 9'sd0;
        sensor2_step = 9'sd0;
        sensor3_step = 9'sd0;

        #400ns;
        #1ns;

        if (file != 0)
            $fclose(file);

        $finish;

    end

endmodule