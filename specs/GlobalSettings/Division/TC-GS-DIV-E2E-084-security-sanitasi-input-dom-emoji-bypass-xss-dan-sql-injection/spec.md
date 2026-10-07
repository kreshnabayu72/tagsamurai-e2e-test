---
id: TC-GS-DIV-E2E-084-security-sanitasi-input-dom-emoji-bypass-xss-dan-sql-injection
title: "Ketahanan Input: Penolakan Emoji Bypass DOM di Server, Sanitasi XSS Nama Divisi, dan Netralisasi SQL Injection pada Kotak Pencarian"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-267
  - TC-GS-DIV-268
  - TC-GS-DIV-269
  - TC-GS-DIV-270
coverage:
  web: automated
---

# Ketahanan Input: Penolakan Emoji Bypass DOM di Server, Sanitasi XSS Nama Divisi, dan Netralisasi SQL Injection pada Kotak Pencarian

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

### Name berisi emoji yang lolos validasi klien tetap ditolak server (TC-GS-DIV-267)

1. Login sbg Total Control
2. Buka Create Division
3. Suntikkan nilai `Finance 😀` langsung ke field Division Name lewat DOM (melewati validasi klien) lalu klik `[Submit]`
4. Verifikasi Division tidak dibuat
5. Verifikasi Modal tetap terbuka dengan input dipertahankan dan penolakan server ditampilkan pada form

### Division Name berisi markup HTML ditampilkan sebagai teks biasa (TC-GS-DIV-268)

6. Buat Division dengan Name `<script>alert(1)</script>` dan Code `XSS1`
7. Lihat baris di tabel, Dialog hapus, dan Modal Changelog
8. Verifikasi Name tampil sebagai teks literal `<script>alert(1)</script>` di tabel, dialog, dan Changelog
9. Verifikasi Tidak ada skrip yang dieksekusi dan tidak ada dialog browser

### Search berisi payload SQL tidak memengaruhi hasil (TC-GS-DIV-269)

10. Cari `' OR '1'='1` lalu Enter pada tabel Division
11. Verifikasi Tabel menampilkan `No results found` (keyword diperlakukan sebagai teks biasa)
12. Verifikasi Tidak ada error server dan tidak ada data yang bocor

### Edit Name berisi emoji yang lolos validasi klien tetap ditolak server (TC-GS-DIV-270)

13. Login sbg Total Control
14. Buka Edit Division `Finance`
15. Suntikkan nilai `Finance 😀` langsung ke field Division Name lewat DOM (melewati validasi klien) lalu klik `[Save]`
16. Verifikasi Perubahan tidak tersimpan dan Name tetap `Finance`
17. Verifikasi Modal tetap terbuka dengan input dipertahankan dan penolakan server ditampilkan pada form

## Notes

- Memvalidasi penolakan server saat validasi emoji dibypass lewat DOM pada Create dan Edit, penampilan payload XSS script (<script>alert(1)</script>) sebagai teks biasa di tabel/dialog/changelog, dan netralisasi query SQL injection (' OR '1'='1) di kotak pencarian (PRD §9.3, §9.4.3).
- Sumber pemetaan test case granular: TC-GS-DIV-267, TC-GS-DIV-268, TC-GS-DIV-269, TC-GS-DIV-270.
