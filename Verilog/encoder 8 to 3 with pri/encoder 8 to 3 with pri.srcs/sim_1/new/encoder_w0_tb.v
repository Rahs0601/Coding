`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.12.2021 19:32:27
// Design Name: 
// Module Name: encoder_w0_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module encoder_wo_tb;
reg [7:0]in_a;
wire [2:0]out_y;
encoder_wo dut0 (out_y, in_a);
initial 
begin
in_a 
=8'b00000001;
#5 in_a =8'b00000010;
#5 in_a =8'b00000100;
#5 in_a =8'b00001000;
#5 in_a =8'b00010000;
#5 in_a =8'b00100000;
#5 in_a =8'b01000000;
#5 in_a =8'b10000000;
#5 $finish;
end
endmodule