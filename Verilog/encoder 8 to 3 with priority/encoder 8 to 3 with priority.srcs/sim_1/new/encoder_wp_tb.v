`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.12.2021 19:37:13
// Design Name: 
// Module Name: encoder_wp_tb
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
reg [7:0]in_a;
wire [2:0]out_y;
encoder_wp dut0 (out_y, in_a);
initial 
begin
in_a 
=8'b00000001;
#5 in_a =8'b0000001x;
#5 in_a =8'b000001xx;
#5 in_a =8'b00001xxx;
#5 in_a =8'b0001xxxx;
#5 in_a =8'b001xxxxx;
#5 in_a =8'b01xxxxxx;
#5 in_a =8'b1xxxxxxx;
#5 $finish;
end
endmodule