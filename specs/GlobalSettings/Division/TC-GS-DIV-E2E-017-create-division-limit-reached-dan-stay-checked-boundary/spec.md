---
id: TC-GS-DIV-E2E-017-create-division-limit-reached-dan-stay-checked-boundary
title: "Pemblokiran Pembuatan Divisi Saat Master Data Count Limit Tercapai"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-28
  - TC-GS-DIV-223
coverage:
  web: automated
---

# Pemblokiran Pembuatan Divisi Saat Master Data Count Limit Tercapai

## Prerequisites

- Login sebagai Role: Total Control
- Jumlah total record divisi pada workspace/entitas dikondisikan telah mencapai nilai master_data_count_limit

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik tombol '[+ Division]'
3. Verifikasi muncul dialog blocker 'Limit Reached' dengan body 'You\'ve reached the division limit for this workspace.' dan tombol tunggal '[OK]'
4. Klik tombol '[OK]' dan verifikasi dialog menutup tanpa membuka form input
5. Kondisikan sisa slot limit tepat 1 data divisi, lalu buka modal Create Division dan centang 'Stay on this form after submitting'
6. Ketik nama divisi valid dan klik '[Submit]'
7. Verifikasi divisi terakhir berhasil dibuat
8. Saat form tetap terbuka untuk input berikutnya, verifikasi sistem mendeteksi limit tercapai sehingga submit selanjutnya diblokir dengan dialog 'Limit Reached'

## Notes

- Menguji ceiling teknis Master Data Count Limit platform sesuai division.md §4.2d Dialog 6 dan §9.5.
