`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.12.2021 19:08:39
// Design Name: 
// Module Name: encoder_wo_tb
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
reg [3:0]in_a;
wire [1:0]out_y;
encoder_wo dut0 (out_y, in_a);
initial 
begin
in_a =4'b0001;
#5 in_a =4'b0010;
#5 in_a =4'b0100;
#5 in_a=4'b1000;
#5
$finish;
end
endmodule