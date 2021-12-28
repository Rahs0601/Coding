`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.12.2021 19:24:11
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

module encoder_wp_tb;
reg [3:0]in_a;
wire [1:0]out_y;
encoder_wp dut0 (out_y, in_a);
initial 
begin
in_a =4'b0001;
#5 in_a =4'b001x;
#5 in_a =4'b01xx;
#5 in_a=4'b1xxx;
#5
$finish;
end
endmodule
