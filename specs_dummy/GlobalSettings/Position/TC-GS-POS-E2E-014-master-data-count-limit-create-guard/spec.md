---
id: TC-GS-POS-E2E-014-master-data-count-limit-create-guard
title: "Volume Data: Penegakan Master Data Count Limit pada tombol [+ Position], submit, dan Stay on this form"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-69
  - TC-GS-POS-70
  - TC-GS-POS-71
  - TC-GS-POS-72
  - TC-GS-POS-259
  - TC-GS-POS-280
coverage:
  web: automated
---

# Volume Data: Penegakan Master Data Count Limit pada tombol [+ Position], submit, dan Stay on this form

## Prerequisites

- Login sebagai Total Control
- Nilai Master Data Count Limit untuk modul Position diatur sama dengan jumlah record Position yang ada saat ini (limit tercapai) melalui konfigurasi Admin Console

## Test Steps

### Klik [+ Position] Saat Limit Tercapai

1. Buka Global Settings > User > Position saat jumlah data telah mencapai Master Data Count Limit
2. Klik tombol primary "[+ Position]"
3. Verifikasi dialog konfirmasi "Limit Reached" muncul dengan pesan bahwa kuota master data telah terpenuhi
4. Klik tombol "[OK]" pada dialog dan verifikasi dialog tertutup tanpa membuka form Create

### Limit Tercapai di Tengah Sesi Form Terbuka

5. Atur limit tersisa 1 slot
6. Buka form Create Position dan centang "[x] Stay on this form after submitting"
7. Masukkan nama Position valid lalu klik "[Submit]"
8. Verifikasi record ke-N berhasil dibuat dan kuota kini penuh
9. Coba lakukan submit record berikutnya dari form yang masih terbuka
10. Verifikasi dialog Limit Reached muncul dan submit ditolak server

## Notes

- Menggabungkan TC-GS-POS-69, 70, 71, 72, 259, dan 280 dalam kelas harness Volume Data Khusus.
