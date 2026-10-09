---
id: TC-GS-GSET-E2E-004-tooltip-info-dan-opsi-dropdown-kelima-field
title: "Tooltip ikon info dan opsi dropdown kelima field: Session Idle Timeout, Date Format, Time Format, Currency Code, dan Time Zone"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-06
  - TC-GS-GSET-07
  - TC-GS-GSET-08
  - TC-GS-GSET-09
  - TC-GS-GSET-10
coverage:
  web: automated
---

# Tooltip ikon info dan opsi dropdown kelima field: Session Idle Timeout, Date Format, Time Format, Currency Code, dan Time Zone

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Tooltip Ikon Info Label

1. Hover ikon info di samping label "Currency Code"
2. Verifikasi tooltip tampil persis "Currency used to display amounts across all products. Changing it does not convert existing amounts."
3. Hover ikon info di samping label "Time Zone"
4. Verifikasi tooltip tampil persis "Time zone used to display dates and times across all products."
5. Hover ikon info di samping label "Session Idle Timeout"
6. Verifikasi tooltip tampil persis "How long a user can stay idle before being logged out automatically."
7. Verifikasi label "Date Format" dan "Time Format" tidak memiliki ikon info

### Opsi Select Session Idle Timeout

8. Klik Select "Session Idle Timeout" dan amati daftar opsi
9. Verifikasi opsi berurutan: `15 minutes`, `30 minutes`, `1 hour`, `2 hours`, `4 hours`, `8 hours`
10. Verifikasi tidak ada opsi "Never" dan tidak ada kotak pencarian di dalam Select

### Opsi Select Date Format dan Time Format

11. Klik Select "Date Format" dan amati opsi
12. Verifikasi lima opsi: `dd/MM/yy` (17/03/23, default), `M/d/yy` (3/17/23), `dd MMM yy` (17 Mar 23), `DDD, MMM dd, yy` (Fri, Mar 17, 23), `DDD, MMM dd, yyyy` (Fri, Mar 17, 2023)
13. Verifikasi tidak ada opsi ISO 8601 `YYYY-MM-DD`
14. Tutup lalu klik Select "Time Format" dan amati opsi
15. Verifikasi dua opsi: `hh:mm a` (02:30 PM) dan `HH:mm` (14:30, default)
16. Verifikasi kedua Select tidak memiliki kotak pencarian (tidak Searchable)

### Select Currency Code Searchable

17. Klik Select "Currency Code" dan amati label opsi
18. Verifikasi setiap label berformat "[Symbol] - [Currency Name]" dengan simbol tampil di label opsi
19. Ketik "Dollar" di kotak pencarian Select
20. Verifikasi daftar menyempit ke opsi yang labelnya memuat "Dollar"
21. Hapus kata kunci lalu ketik "Euro" dan pilih opsi untuk kode `EUR`
22. Verifikasi field menampilkan label opsi `EUR` yang dipilih
23. Verifikasi tidak ada opsi "Other" dan tidak ada field "Currency Symbol" terpisah

### Select Time Zone Searchable

24. Klik Select "Time Zone" dan catat label opsi terpilih (default `Asia/Jakarta`)
25. Verifikasi label tiap opsi berformat "(UTC±HH:MM) City1, City2, City3"
26. Ketik di kotak pencarian salah satu nama kota yang ada di label opsi `Asia/Jakarta`
27. Verifikasi opsi yang sama ditemukan
28. Hapus kata kunci lalu ketik "zzzz"
29. Verifikasi tidak ada opsi yang cocok

## Notes

- Menggabungkan pengujian tooltip ikon info dan isi opsi dropdown kelima field (TC-GS-GSET-06 s.d. TC-GS-GSET-10). Halaman dibuka satu kali; Select ditutup dan dibuka di antara kasus.
