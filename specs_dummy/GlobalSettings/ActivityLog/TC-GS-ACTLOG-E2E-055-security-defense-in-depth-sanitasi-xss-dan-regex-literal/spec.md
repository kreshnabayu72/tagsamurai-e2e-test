---
id: TC-GS-ACTLOG-E2E-055-security-defense-in-depth-sanitasi-xss-dan-regex-literal
title: "Security & Defense-in-Depth: Sanitasi Payload XSS di Kotak Pencarian dan Sel Tabel serta Pencocokan String Regex Literal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-218
  - TC-GS-ACTLOG-219
  - TC-GS-ACTLOG-220
coverage:
  web: automated
---

# Security & Defense-in-Depth: Sanitasi Payload XSS di Kotak Pencarian dan Sel Tabel serta Pencocokan String Regex Literal

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat entri Brand dengan nama payload XSS '<img src=x onerror=alert(1)>' pada Tab User Action

## Test Steps

### Sanitasi XSS di Search Box Tab Session
1. Buka Tab Session, masukkan payload '<script>alert(1)</script>' pada Search box lalu tekan Enter.
2. Verifikasi tidak ada dialog peringatan JavaScript alert yang muncul di peramban.
3. Verifikasi tabel menampilkan 'No results found'.
### Sanitasi XSS di Search Box Tab User Action
4. Pindah ke Tab User Action, masukkan payload script yang sama di Search box.
5. Verifikasi script tidak dieksekusi dan tabel menampilkan 'No results found'.
### Sanitasi Stored XSS pada Sel Tabel
6. Cari entri Brand dengan nama '<img src=x onerror=alert(1)>' di Tab User Action.
7. Verifikasi sel Name dan New Value merender teks mentah apa adanya (escaped HTML) tanpa merender elemen gambar atau memicu script.
### Karakter Pola Regex Literal
8. Masukkan karakter pola regex '.*' di kotak Search kedua tab.
9. Verifikasi string diperlakukan sebagai teks harfiah (menampilkan 'No results found' dan tidak mencocokkan seluruh baris).

## Notes

- Antarmuka aman dari celah Stored XSS maupun Reflected XSS, dan parser pencarian memperlakukan karakter regex secara harfiah.
