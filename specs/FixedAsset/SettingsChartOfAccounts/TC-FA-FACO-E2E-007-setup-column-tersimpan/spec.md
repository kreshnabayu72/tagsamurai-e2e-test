---
id: TC-FA-FACO-E2E-007-setup-column-tersimpan
title: "Konfigurasi kolom Account List dan Changelog bertahan sesudah muat ulang"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#b3", "§5#b11", "EB-SRC-5@tabel-account-list", "EB-SRC-5@tabel-changelog", "EB-KOL-2@tabel-account-list", "EB-KOL-2@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "§5#b3": 7
  "§5#b11": [18, 20]
  "EB-SRC-5@tabel-account-list": [7, 12]
  "EB-SRC-5@tabel-changelog": [34, 39]
  "EB-KOL-2@tabel-account-list": 18
  "EB-KOL-2@tabel-changelog": 47
anchor: [2, 17, 29, 46]
coverage:
  web: automated
---

# Konfigurasi kolom Account List dan Changelog bertahan sesudah muat ulang

## Prerequisites
- Aktor: pengguna Total Control. Aktor lain: Admin B (DU-007-2).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-007-1: akun `X1-{runId}`, Account Name `Kolom Uji {runId}`, Account Function `Asset Cost`, Status `Active`. Account Name sesudah Edit: `Kolom Uji B {runId}`.
  - DU-007-2: Admin B, nama `Admin B {runId}`, role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2. Belum pernah mengubah konfigurasi kolom di browser-nya.

## Test Steps
### Kolom yang di-hide tidak ikut dicari di Account List dan cocok lagi saat ditampilkan
1. Ketik Search `Kolom Uji {runId}`, tekan Enter
2. Verifikasi baris `X1-{runId}` tampil
3. Klik header kolom Actions `⋯`
4. Hapus centang `Account Name` pada panel Column Visibility
5. Klik header kolom Actions `⋯` untuk menutup panel
6. Tekan Enter pada kotak Search
7. Verifikasi `No results found` tampil karena kolom Account Name di-hide
8. Klik header kolom Actions `⋯`
9. Centang `Account Name` pada panel Column Visibility
10. Klik header kolom Actions `⋯` untuk menutup panel
11. Tekan Enter pada kotak Search
12. Verifikasi baris `X1-{runId}` tampil kembali karena kolom Account Name ditampilkan

### Konfigurasi kolom Account List bertahan sesudah muat ulang dan tidak memengaruhi pengguna lain
13. Klik header kolom Actions `⋯`
14. Hapus centang `Function` pada panel Column Visibility
15. Klik header kolom Actions `⋯` untuk menutup panel
16. Muat ulang halaman
17. Verifikasi header kolom `Account Code` tampil
18. Verifikasi header kolom `Function` tidak tampil sesudah muat ulang halaman
19. Admin B membuka Settings > Accounting > Chart of Accounts pada sesi dan browser miliknya
20. Verifikasi header kolom `Function` tampil di layar Admin B
21. Klik header kolom Actions `⋯`
22. Centang `Function` pada panel Column Visibility
23. Klik header kolom Actions `⋯` untuk menutup panel

### Kolom yang di-hide tidak ikut dicari di modal Changelog dan cocok lagi saat ditampilkan
24. Klik `⋯` pada baris `X1-{runId}` > `Edit`
25. Ganti isi Account Name dengan `Kolom Uji B {runId}`
26. Klik `[Save]`
27. Klik ikon Changelog
28. Ketik Search `Kolom Uji {runId}` pada modal Changelog, tekan Enter
29. Verifikasi entri dengan Account Code `X1-{runId}` tampil di modal Changelog
30. Klik header kolom Actions `⋯` pada tabel Changelog
31. Hapus centang `Old Value` pada panel Column Visibility
32. Klik header kolom Actions `⋯` untuk menutup panel
33. Tekan Enter pada kotak Search modal Changelog
34. Verifikasi `No results found` tampil di modal Changelog karena kolom Old Value di-hide
35. Klik header kolom Actions `⋯` pada tabel Changelog
36. Centang `Old Value` pada panel Column Visibility
37. Klik header kolom Actions `⋯` untuk menutup panel
38. Tekan Enter pada kotak Search modal Changelog
39. Verifikasi entri dengan Account Code `X1-{runId}` tampil kembali di modal Changelog karena kolom Old Value ditampilkan

### Konfigurasi kolom modal Changelog bertahan sesudah muat ulang
40. Klik header kolom Actions `⋯` pada tabel Changelog
41. Klik `Setup Column...`
42. Hapus centang `Field` pada modal Setup Column
43. Klik `[Save]`
44. Muat ulang halaman
45. Klik ikon Changelog
46. Verifikasi header kolom `Account Code` tampil di modal Changelog
47. Verifikasi header kolom `Field` tidak tampil di modal Changelog sesudah muat ulang halaman
48. Klik header kolom Actions `⋯` pada tabel Changelog
49. Centang `Field` pada panel Column Visibility
50. Klik header kolom Actions `⋯` untuk menutup panel
