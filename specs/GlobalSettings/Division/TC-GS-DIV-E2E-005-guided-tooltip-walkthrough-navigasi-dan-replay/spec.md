---
id: TC-GS-DIV-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay
title: "Guided Tooltip 3-Step Walkthrough, Navigasi Tombol, Keyboard, dan Replay"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-216
  - TC-GS-DIV-217
  - TC-GS-DIV-218
  - TC-GS-DIV-219
  - TC-GS-DIV-221
coverage:
  web: automated
---

# Guided Tooltip 3-Step Walkthrough, Navigasi Tombol, Keyboard, dan Replay

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Flag guided_tooltip_seen_gs-division belum terpasang (kunjungan pertama kali)

## Test Steps

1. Buka menu Global Settings > User > tab Division untuk pertama kali
2. Verifikasi walkthrough otomatis muncul pada Step 1 menargetkan tombol '[+ Division]' (#btn-add-division) dengan judul 'Add Division', deskripsi 'Tambahkan divisi departemen baru untuk mengelompokkan struktur organisasi akun staf Anda.', indikator 'Step 1 of 3', tombol '[Back]' tersembunyi, dan tombol '[Next]' aktif
3. Tekan tombol panah kanan (→) atau klik '[Next]'
4. Verifikasi walkthrough beralih ke Step 2 menargetkan tabel (#table-division-list) dengan judul 'Division Table', deskripsi 'Daftar seluruh departemen aktif di perusahaan Anda dikelola pada tabel ini.', dan tombol '[Back]' tampil aktif
5. Tekan tombol panah kiri (←) atau klik '[Back]'
6. Verifikasi walkthrough kembali ke Step 1
7. Klik '[Next]' dua kali menuju Step 3 menargetkan tombol Changelog (#btn-division-changelog) dengan judul 'Changelog Audit', deskripsi 'Tinjau riwayat penambahan dan pengeditan nama divisi secara lengkap di sini.', dan tombol '[Next]' berubah label menjadi '[Done]'
8. Klik tombol '[Done]'
9. Verifikasi walkthrough tertutup dan flag seen tersimpan di local storage / user preference
10. Refresh halaman dan verifikasi walkthrough TIDAK muncul otomatis kembali
11. Klik ikon bantuan '[?]' di area header breadcrumb
12. Verifikasi walkthrough mulai terbuka kembali secara manual dari Step 1
13. Tekan tombol Escape (Esc) pada keyboard dan verifikasi walkthrough langsung tertutup

## Notes

- Langkah walkthrough kanonikal terdiri dari 3 step sesuai PRD division.md §4.7 (page_key: gs-division), memperbaiki deskripsi usang 2-step pada TC lama.
