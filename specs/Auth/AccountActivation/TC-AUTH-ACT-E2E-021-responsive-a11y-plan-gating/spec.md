---
id: TC-AUTH-ACT-E2E-021-responsive-a11y-plan-gating
title: Responsive, accessibility (A11y), dan Plan Gating
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-85
  - TC-AUTH-ACT-86
  - TC-AUTH-ACT-87
  - TC-AUTH-ACT-88
  - TC-AUTH-ACT-89
  - TC-AUTH-ACT-90
  - TC-AUTH-ACT-91
  - TC-AUTH-ACT-92
coverage:
  web: automated
---

# Responsive, accessibility (A11y), dan Plan Gating

## Prerequisites

- Token valid `active` tersedia untuk menguji halaman Set Password dalam berbagai viewport.
- Halaman `/activate?token={validToken}`, halaman Activation Success, dan halaman 404 aktivasi dapat diakses.
- Kemampuan mengubah viewport browser (resize) untuk menguji responsive design.
- Tools/access untuk melakukan accessibility checks dasar (focus visibility, keyboard navigation) sesuai kemampuan otomasi.
- Untuk Plan Gating (TC-AUTH-ACT-92), diperlukan setup state plan sesuai lingkungan test. Jika skenario plan gating bergantung pada kondisi yang tidak bisa dipicu dengan aman di backend nyata, gunakan `Spectra.intercept()` jika diperlukan. Mode: mock sesuai kebutuhan.
- Beberapa skenario responsive/a11y bersifat UI-focused.

## Test Steps

### A. Responsive & layout

1. Buka halaman Set Password dengan token valid.
2. Ubah viewport ke ukuran mobile (misalnya 375x667 / 390x844) sesuai breakpoint aplikasi.
3. Verifikasi layout halaman tetap terbaca, field Password dan Confirm Password tidak terpotong, tombol `[Set Password]` tetap terlihat dan dapat diklik.
4. Verifikasi checklist 6 baris Password Policy tetap tampil dengan layout yang sesuai di viewport mobile (tidak overflow, tetap terbaca).
5. Ubah viewport ke ukuran tablet (768x1024) dan verifikasi layout responsif.
6. Kembalikan ke viewport desktop (1280x800+) dan verifikasi layout normal.
7. Ulangi verifikasi responsive pada halaman Activation Success (setelah aktivasi) di viewport mobile.
8. Ulangi verifikasi responsive pada halaman 404 aktivasi (varian Expired dan Used) di viewport mobile.

### B. Accessibility (A11y) - focus & keyboard

9. Buka halaman Set Password di viewport desktop.
10. Navigasi menggunakan Tab key untuk berpindah antar elemen (field Email/Password context, field Password, field Confirm Password, ikon mata, tombol `[Set Password]`, link jika ada).
11. Verifikasi setiap elemen interaktif yang difokus memiliki focus ring yang terlihat jelas.
12. Verifikasi ikon mata (eye icon) dapat difokus dan di-toggle via keyboard (Enter/Space) - konsisten dengan TC-AUTH-ACT-37.
13. Verifikasi urutan fokus (tab order) logis dan tidak meloncat secara tidak terduga.
14. Isi form dengan nilai valid menggunakan keyboard navigation saja (Tab untuk pindah field, ketik, Space/Enter untuk submit).
15. Verifikasi form dapat disubmit sepenuhnya menggunakan keyboard tanpa mouse.

### C. Accessibility - readability & contrast (dasar)

16. Verifikasi teks pada halaman (label, subtitle, error message, checklist) tetap terbaca di viewport mobile dan tidak bertumpuk dengan buruk.
17. Verifikasi pesan error inline (password mismatch/empty) tetap terlihat dan tidak terpotong saat muncul.
18. Verifikasi state error dan state normal dibedakan secara visual (sesuai styling aplikasi).

### D. Plan Gating

19. Siapkan kondisi Plan Gating sesuai skenario TC-AUTH-ACT-92 (sesuai environment test dan konfigurasi plan).
20. Akses alur Account Activation dalam kondisi plan gating yang relevan.
21. Verifikasi perilaku Plan Gating diterapkan sesuai spesifikasi modul Account Activation (jika ada gating terkait plan pada alur ini).
22. Verifikasi pesan/error terkait plan gating (jika muncul) ditampilkan dengan benar dan sesuai copy aplikasi.
23. Verifikasi alur tetap konsisten dengan behavior yang ditetapkan untuk fitur ini.

## Notes

- TC-AUTH-ACT-85–91 merupakan bagian L (Responsive & A11y), TC-AUTH-ACT-92 bagian M (Plan Gating) - digabung dalam satu spec karena topik UI/behavioral lintas environment dan umumnya tidak memerlukan setup data kompleks terpisah.
- Verifikasi a11y bersifat dasar (focus visibility, keyboard navigation, tab order). Pengujian a11y lebih komprehensif dapat dilakukan terpisah sesuai tools yang tersedia.
- Untuk Plan Gating, jika skenario tidak dapat direproduksi di environment otomasi saat ini, kebutuhan teknis dan asumsi dicatat di Prerequisites tanpa mengubah isi TC sumber.
- Responsive diuji minimal di mobile, tablet, desktop untuk memastikan layout tidak rusak di viewport kecil.
