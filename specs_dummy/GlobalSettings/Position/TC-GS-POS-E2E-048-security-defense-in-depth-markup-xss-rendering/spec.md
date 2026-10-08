---
id: TC-GS-POS-E2E-048-security-defense-in-depth-markup-xss-rendering
title: "Defense-in-depth: Input Position Name berisi markup HTML/XSS dirender sebagai teks murni tanpa eksekusi"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-266
coverage:
  web: automated
---

# Defense-in-depth: Input Position Name berisi markup HTML/XSS dirender sebagai teks murni tanpa eksekusi

## Prerequisites

- Login sebagai Total Control
- Form Create Position dibuka

## Test Steps

### Uji Injeksi Script & Tag HTML

1. Buka form Create Position
2. Masukkan teks yang memuat tag script dan tag HTML: "<script>alert('xss')</script><b>Security Lead</b>"
3. Klik tombol "[Submit]"
4. Verifikasi record berhasil disimpan
5. Amati tampilan baris di tabel utama Position
6. Verifikasi tidak ada dialog alert browser yang muncul (script tidak dieksekusi)
7. Verifikasi tag HTML dirender sebagai teks literal biasa (karakter "<" dan ">" ter-escape secara aman di DOM)
8. Buka Popup Changelog, verifikasi entri juga merender teks secara aman

## Notes

- Menguji defense-in-depth XSS dan encoding tag HTML pada UI (TC-GS-POS-266).
