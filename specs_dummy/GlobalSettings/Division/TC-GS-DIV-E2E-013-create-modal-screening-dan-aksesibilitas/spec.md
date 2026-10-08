---
id: TC-GS-DIV-E2E-013-create-modal-screening-dan-aksesibilitas
title: "Screening Modal Create Division: Tata Letak, Placeholder, Helper Text, AutoFocus, dan Aksesibilitas ARIA"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-31
  - TC-GS-DIV-32
  - TC-GS-DIV-33
coverage:
  web: automated
---

# Screening Modal Create Division: Tata Letak, Placeholder, Helper Text, AutoFocus, dan Aksesibilitas ARIA

## Prerequisites

- Login sebagai Role: Total Control
- User berada di Global Settings > User > Division

## Test Steps

### Screening Popup Create Division (TC-GS-DIV-31)

1. Klik `[+ Division]`
2. Verifikasi Title `Create Division`
3. Verifikasi Icon close `[✕]`
4. Verifikasi Field `Division Name *` dengan placeholder `Enter division name`
5. Verifikasi Field `Code` dengan placeholder `Enter code, or leave blank to auto-generate`
6. Verifikasi Helper text Code (selalu tampil): `Letters, numbers, hyphens, underscores, and dots only`
7. Verifikasi Checkbox `Stay on this form after submitting` unchecked secara default
8. Verifikasi Tombol `[Clear Field]` (text, primary) dan `[Submit]` (filled, success) rata kanan; tidak ada tombol `[Cancel]`

### Accessibility Popup Create Division: fokus awal, aria, focus trap, Esc (TC-GS-DIV-32)

9. Klik `[+ Division]`
10. Perhatikan elemen yang mendapat fokus
11. Kosongkan Name lalu klik `[Submit]` dan periksa atribut field Name
12. Tekan Tab berulang melewati seluruh elemen
13. Tekan Esc
14. Verifikasi Kursor otomatis fokus pada input Division Name saat modal terbuka
15. Verifikasi Field Division Name memiliki `aria-required="true"` dan error field terhubung lewat `aria-describedby`
16. Verifikasi Fokus keyboard tidak keluar dari modal (focus trap)
17. Verifikasi Esc menutup modal tanpa dialog karena form kosong

### Tombol Submit masuk Saving state dan seluruh kontrol form disabled (TC-GS-DIV-33)

18. Klik `[+ Division]`
19. Tahan (delay) respons simpan di network
20. Isi Division Name `Procurement Team`
21. Klik `[Submit]`
22. Perhatikan tombol dan kontrol form sebelum respons datang
23. Verifikasi Tombol `[Submit]` menampilkan spinner dan disabled
24. Verifikasi Seluruh kontrol form dan icon `[✕]` ikut disabled hingga proses simpan selesai
25. Verifikasi Hover `[Submit]` sebelum diklik menampilkan background success hover

## Notes

- Memvalidasi struktur visual modal Create Division (size md), header, field Division Name *, Code opsional, helper text, autofocus, dan atribut ARIA (PRD §4.2c, §4.5).
- Sumber pemetaan test case granular: TC-GS-DIV-31, TC-GS-DIV-32, TC-GS-DIV-33.
