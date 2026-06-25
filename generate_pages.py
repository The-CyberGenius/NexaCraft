import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Update Footer in index_html
new_footer = """
    <footer style="padding: 60px 0 20px; background: var(--bg-secondary); border-top: 1px solid var(--border-color);">
        <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; margin-bottom: 40px; text-align: left;">
            <div>
                <h3 style="font-size: 1.5rem; color: var(--text-primary); margin-bottom: 15px;">Vaishnavi <span style="color: var(--accent);">Web Crafter</span></h3>
                <p style="color: var(--text-secondary); font-size: 0.95rem; line-height: 1.6;">Engineering high-end digital products and scalable solutions for ambitious brands.</p>
                <div style="margin-top: 20px; display: flex; gap: 15px;">
                    <a href="#" style="color: var(--text-secondary); font-size: 1.2rem; transition: color var(--transition);"><i class="fa-brands fa-linkedin"></i></a>
                    <a href="#" style="color: var(--text-secondary); font-size: 1.2rem; transition: color var(--transition);"><i class="fa-brands fa-twitter"></i></a>
                    <a href="#" style="color: var(--text-secondary); font-size: 1.2rem; transition: color var(--transition);"><i class="fa-brands fa-instagram"></i></a>
                </div>
            </div>
            <div>
                <h4 style="color: var(--text-primary); margin-bottom: 20px; font-weight: 600;">Company</h4>
                <ul style="display: flex; flex-direction: column; gap: 12px;">
                    <li><a href="about.html" style="color: var(--text-secondary); font-size: 0.95rem; transition: color var(--transition);">About Us</a></li>
                    <li><a href="services.html" style="color: var(--text-secondary); font-size: 0.95rem; transition: color var(--transition);">Services</a></li>
                    <li><a href="portfolio.html" style="color: var(--text-secondary); font-size: 0.95rem; transition: color var(--transition);">Portfolio</a></li>
                    <li><a href="contact.html" style="color: var(--text-secondary); font-size: 0.95rem; transition: color var(--transition);">Contact</a></li>
                </ul>
            </div>
            <div>
                <h4 style="color: var(--text-primary); margin-bottom: 20px; font-weight: 600;">Legal</h4>
                <ul style="display: flex; flex-direction: column; gap: 12px;">
                    <li><a href="terms.html" style="color: var(--text-secondary); font-size: 0.95rem; transition: color var(--transition);">Terms & Conditions</a></li>
                    <li><a href="privacy.html" style="color: var(--text-secondary); font-size: 0.95rem; transition: color var(--transition);">Privacy Policy</a></li>
                    <li><a href="refund.html" style="color: var(--text-secondary); font-size: 0.95rem; transition: color var(--transition);">Cancellation & Refund</a></li>
                </ul>
            </div>
            <div>
                <h4 style="color: var(--text-primary); margin-bottom: 20px; font-weight: 600;">Contact</h4>
                <ul style="display: flex; flex-direction: column; gap: 12px;">
                    <li style="color: var(--text-secondary); font-size: 0.95rem; display: flex; align-items: flex-start; gap: 10px;">
                        <i class="fa-solid fa-location-dot" style="margin-top: 4px; color: var(--accent);"></i> Tech Park, Cyber City, Workspace 402
                    </li>
                    <li style="color: var(--text-secondary); font-size: 0.95rem; display: flex; align-items: center; gap: 10px;">
                        <i class="fa-brands fa-whatsapp" style="color: #25D366;"></i> +91 8368435458
                    </li>
                </ul>
            </div>
        </div>
        <div style="border-top: 1px solid var(--border-color); padding-top: 20px; text-align: center; color: var(--text-muted); font-size: 0.85rem;">
            &copy; 2026 Vaishnavi Web Crafter. All rights reserved.
        </div>
    </footer>
"""

# Replace footer in index
index_html = re.sub(r'<footer>.*?</footer>', new_footer, index_html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Extract Template Parts
head_part = index_html.split('<section class="hero')[0]
footer_part = index_html.split('</section>')[-1] # Gets the footer and scripts

# Fix active links in nav for subpages
head_part_sub = head_part.replace('<a href="#hero" class="active">Home</a>', '<a href="index.html">Home</a>')
head_part_sub = head_part_sub.replace('href="#', 'href="index.html#') # Fix hash links

def create_page(filename, title, content):
    html = head_part_sub.replace('<title>Vaishnavi Web Crafter', f'<title>{title} | Vaishnavi Web Crafter')
    
    # Simple Hero for inner pages
    hero = f"""
    <section class="hero reveal" style="min-height: 40vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 100px;">
        <div class="container">
            <h1 class="section-title" style="font-size: clamp(2.5rem, 5vw, 4rem);">{title}</h1>
        </div>
    </section>
    """
    
    page = html + hero + content + footer_part
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page)

# 1. Terms
terms_content = """
<section class="reveal" style="padding: 60px 0 100px; background: var(--bg-primary);">
    <div class="container" style="max-width: 800px; color: var(--text-secondary); line-height: 1.8;">
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">1. Introduction</h3>
        <p style="margin-bottom: 30px;">Welcome to Vaishnavi Web Crafter. By accessing our website and using our services, you agree to be bound by the following terms and conditions. Please read them carefully.</p>
        
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">2. Services Rendered</h3>
        <p style="margin-bottom: 30px;">We provide high-end web development, UI/UX design, and digital branding services. All project scopes, timelines, and deliverables will be clearly outlined in a separate Service Level Agreement (SLA) or contract prior to project commencement.</p>
        
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">3. Payment Terms</h3>
        <p style="margin-bottom: 30px;">An upfront deposit is required to begin work. The remaining balance will be due upon project completion or at agreed-upon milestones. We accept bank transfers, UPI, and major credit cards.</p>
        
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">4. Intellectual Property</h3>
        <p style="margin-bottom: 30px;">Upon final payment, all intellectual property rights for the developed website/application are transferred to the client. Pre-existing frameworks or proprietary code remain the property of Vaishnavi Web Crafter and are licensed to the client.</p>
    </div>
</section>
"""
create_page('terms.html', 'Terms & Conditions', terms_content)

# 2. Privacy
privacy_content = """
<section class="reveal" style="padding: 60px 0 100px; background: var(--bg-primary);">
    <div class="container" style="max-width: 800px; color: var(--text-secondary); line-height: 1.8;">
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">1. Data Collection</h3>
        <p style="margin-bottom: 30px;">We respect your privacy. We collect only the information necessary to provide our digital services, such as your name, email, phone number, and project requirements when you use our contact forms.</p>
        
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">2. Use of Information</h3>
        <p style="margin-bottom: 30px;">Your information is used strictly to communicate regarding your project, send invoices, and deliver technical support. We do not sell or share your data with third-party marketing agencies.</p>
        
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">3. Security</h3>
        <p style="margin-bottom: 30px;">We implement robust security protocols to protect your personal and project data from unauthorized access, alteration, or disclosure.</p>
    </div>
</section>
"""
create_page('privacy.html', 'Privacy Policy', privacy_content)

# 3. Refund
refund_content = """
<section class="reveal" style="padding: 60px 0 100px; background: var(--bg-primary);">
    <div class="container" style="max-width: 800px; color: var(--text-secondary); line-height: 1.8;">
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">1. Cancellation Policy</h3>
        <p style="margin-bottom: 30px;">Clients may cancel a project within 48 hours of initial payment for a full refund, provided no active development or design work has commenced.</p>
        
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">2. Refund Eligibility</h3>
        <p style="margin-bottom: 30px;">Because we invest significant time and resources into custom digital products, refunds are evaluated on a case-by-case basis. If the project is canceled after work has begun, we will retain a portion of the deposit equivalent to the billable hours completed.</p>
        
        <h3 style="color: var(--text-primary); margin-bottom: 20px;">3. Maintenance Plans</h3>
        <p style="margin-bottom: 30px;">Monthly or annual maintenance and hosting plans can be canceled at any time, but previously paid cycles are non-refundable.</p>
    </div>
</section>
"""
create_page('refund.html', 'Cancellation & Refund', refund_content)

# 4. About (Extracted from index)
about_content = """
<section class="about reveal" style="background: var(--bg-primary); padding: 60px 0 100px; border-bottom: 1px solid var(--border-color);">
    <div class="container">
        <div class="about-grid" style="display: grid; gap: 60px; align-items: center;">
            <div class="about-image" style="position: relative; border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow-lg);">
                <img src="assets/team.png" alt="Vaishnavi and the Elite Tech Team" style="width: 100%; height: auto; display: block; transform: scale(1.02); transition: transform 0.5s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1.02)'">
                <div style="position: absolute; bottom: 20px; left: 20px; background: rgba(0,0,0,0.6); backdrop-filter: blur(10px); padding: 10px 20px; border-radius: 50px; color: #fff; font-weight: 600; font-size: 0.9rem; border: 1px solid rgba(255,255,255,0.2);">
                    <i class="fa-solid fa-users" style="color: #25D366; margin-right: 8px;"></i> A Real Team, Real Results
                </div>
            </div>
            <div class="about-content" style="max-width: 600px;">
                <h2 class="section-title" style="margin-bottom: 24px; font-size: clamp(2rem, 4vw, 2.5rem);">Hi, I'm Vaishnavi! 👋</h2>
                <p style="color: var(--text-secondary); font-size: 1.15rem; line-height: 1.7; margin-bottom: 20px;">
                    I believe that behind every great digital experience is a dedicated team of real people. My elite team of developers and designers doesn't just write code—we craft solutions with care, passion, and precision.
                </p>
                <p style="color: var(--text-secondary); font-size: 1.15rem; line-height: 1.7; margin-bottom: 30px;">
                    Whether you need a simple landing page or a complex corporate web application, we have the technical firepower to bring your vision to life. <strong style="color: var(--text-primary);">Let's build something amazing together.</strong>
                </p>
            </div>
        </div>
    </div>
</section>
"""
create_page('about.html', 'About Us', about_content)

# 5. Services & 6. Portfolio & 7. Contact (I will extract these from index_html so they mirror the homepage but standalone)
def extract_section(section_id):
    pattern = f'<section class="[^"]*{section_id}[^"]*".*?</section>'
    match = re.search(pattern, index_html, flags=re.DOTALL)
    if match:
        return match.group(0)
    # Contact is a bit different
    pattern_contact = r'<section class="[^"]*contact[^"]*".*?</section>'
    match = re.search(pattern_contact, index_html, flags=re.DOTALL)
    if match: return match.group(0)
    return ""

create_page('services.html', 'Our Services', extract_section('services'))
create_page('portfolio.html', 'Our Portfolio', extract_section('portfolio'))
create_page('contact.html', 'Contact Us', extract_section('contact'))


create_page('faq.html', 'Frequently Asked Questions', extract_section('faq'))
