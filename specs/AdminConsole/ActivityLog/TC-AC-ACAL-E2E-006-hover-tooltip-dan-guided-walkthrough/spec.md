---
id: TC-AC-ACAL-E2E-006-hover-tooltip-dan-guided-walkthrough
title: "Hover tooltip teks panjang terpotong dan siklus lengkap Guided Tooltip Walkthrough"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-257
  - TC-AC-ACAL-258
  - TC-AC-ACAL-264
coverage:
  web: automated
---

# Hover tooltip teks panjang terpotong dan siklus lengkap Guided Tooltip Walkthrough

## Prerequisites

- Login sebagai Role: Principal Total Control
- Akun memiliki status kunjungan pertama (flag `guided_tooltip_seen_ac-activity-log` bernilai `false`)
- Terdapat baris data dengan nama User atau Modified By panjang yang terpotong secara visual

## Test Steps

### Auto-trigger Walkthrough Kunjungan Pertama

1. Buka menu `Admin Console > Activity Log`
2. Verifikasi walkthrough Guided Tooltip otomatis muncul pada Step 1
3. Verifikasi Step 1 menargetkan elemen Table dengan judul `"Activity Log"` dan tombol `[Back]` dalam kondisi tersembunyi (Hidden)
4. Klik tombol `[Next]` untuk berpindah ke Step 2
5. Verifikasi Step 2 menargetkan tombol Filter pada toolbar dengan judul `"Filter & Search"`
6. Klik tombol `[Next]` untuk berpindah ke Step 3
7. Verifikasi Step 3 menargetkan tombol Download dengan judul `"Download Log"` dan label tombol berubah menjadi `[Done]`
8. Klik tombol `[Done]` dan verifikasi walkthrough tertutup serta flag seen tersimpan

### Manual Replay, Siklus Tombol & Dismiss Walkthrough

9. Refresh halaman dan verifikasi walkthrough tidak muncul secara otomatis lagi
10. Klik icon bantuan `[?]` pada header halaman
11. Verifikasi walkthrough mulai kembali dari Step 1
12. Klik tombol `[Skip]` dan verifikasi walkthrough langsung tertutup
13. Klik kembali icon `[?]`, lalu klik area overlay gelap di luar modal walkthrough
14. Verifikasi walkthrough tertutup

### Hover Tooltip Teks Terpotong

15. Arahkan kursor mouse (hover) pada sel nama User yang terpotong di Tab Session
16. Verifikasi tooltip muncul menampilkan nama lengkap asli user
17. Klik tab `"User Action"` dan hover pada sel Modified By yang terpotong
18. Verifikasi tooltip menampilkan nama lengkap user pemodifikasi

## Notes

- Walkthrough guided tooltip membantu pengguna baru mengenali 3 zona kontrol utama halaman Activity Log.
