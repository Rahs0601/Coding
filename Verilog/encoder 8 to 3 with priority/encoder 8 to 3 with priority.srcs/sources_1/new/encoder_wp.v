`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 08.12.2021 19:36:14
// Design Name: 
// Module Name: encoder_wp
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


module encoder_wp(out_y, in_a);
input [7:0]in_a;
output reg [2:0]out_y;
always@(in_a)
begin
casex(in_a)
8'b00000001:out_y = 3'b000;
8'b0000001x:out_y = 3'b001;
8'b000001xx:out_y = 3'b010;
8'b00001xxx:out_y = 3'b011;
8'b0001xxxx:out_y = 3'b100;
8'b001xxxxx:out_y = 3'b101;
8'b01xxxxxx:out_y = 3'b110;
8'b1xxxxxxx:out_y = 3'b111;
default:$display("Error!");
endcase
end
endmodule
