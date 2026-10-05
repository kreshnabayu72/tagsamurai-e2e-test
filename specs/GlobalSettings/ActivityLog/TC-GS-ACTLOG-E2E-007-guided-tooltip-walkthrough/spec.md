---
id: TC-GS-ACTLOG-E2E-007-guided-tooltip-walkthrough
title: "Siklus lengkap Guided Tooltip walkthrough, navigasi, auto-trigger, dan manual replay"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-20
  - TC-GS-ACTLOG-21
  - TC-GS-ACTLOG-22
  - TC-GS-ACTLOG-23
  - TC-GS-ACTLOG-24
coverage:
  web: automated
---

# Siklus lengkap Guided Tooltip walkthrough, navigasi, auto-trigger, dan manual replay

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control
- Kunci localStorage `guided_tooltip_seen_gs-activity-log` bernilai false pada awal pengujian

## Test Steps

### Kunjungan Pertama & Navigasi
1. Buka menu `Global Settings > Activity Log`
2. Verifikasi walkthrough otomatis muncul menunjuk ke komponen Tabs
3. Verifikasi Step 1 menampilkan judul "Two Kinds of Activity" dan tombol `[Back]` tersembunyi (Hidden)
4. Klik tombol `[Next]`
5. Verifikasi walkthrough berpindah ke Step 2 menunjuk icon Filter dengan judul "Narrow Down the Log"
6. Verifikasi tombol berubah menjadi `[Done]` dan tombol `[Back]` kini tampil
7. Klik tombol `[Back]` dan verifikasi kembali ke Step 1
8. Klik tombol `[Next]` menuju Step 2
9. Klik tombol `[Done]` untuk menyelesaikan walkthrough
### Replay & Pembatalan
10. Muat ulang halaman (F5) dan verifikasi walkthrough tidak muncul otomatis lagi
11. Klik icon bantuan `[?]` di header
12. Verifikasi walkthrough terbuka kembali mulai dari Step 1
13. Klik pada overlay gelap (Skip) dan verifikasi walkthrough langsung tertutup
14. Buka kembali walkthrough via `[?]`, ubah ukuran viewport browser, dan verifikasi walkthrough tertutup tanpa merusak status selesai

## Notes

- Flag seen disimpan di client storage agar tidak mengganggu admin yang sudah memahami navigasi 2 tab.
