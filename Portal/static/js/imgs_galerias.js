
$(document).ready(function(){		
		$('#cont-list-img >div>a>img').click(function(){
				var elemento = $(this);
				$("#myCarousel")
				.carousel(parseInt($(this).attr('class')))				
				/*.on('slid.bs.carousel', function () { 
						if($(this).find('.active').find('.pie_foto').length > 0){
							if($('#visor').hasClass('chico') || !$('#visor').hasClass('grande'){
								$('#myCarousel').parent()
								.animate({
									height: $('#visor').height()+57		
								})
								.find('ul')
								.animate({
									height:27,
									paddingTop:5
								})
							}
								
						}
						else{
							$('#myCarousel').parent()
							.animate({
								height: $('#visor').height()-57	
							})
							.find('ul')
							.animate({
								height:22,
								paddingTop:2
							})
						}				
				})*/
		})

})
