---
id: TC-FA-FACO-BE-158-search-sort-filter
title: "Hasil Search, Sort, dan Filter daftar akun"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
owner: BE
sourceRules: [EB-SRC-1, EB-FLT-3, EB-SRT-1, EB-SRT-2]
smoke: []
dependsOn: []
trace:
  EB-SRC-1: [2, 4, 6, 8, 10, 12, 14, 16]
  EB-FLT-3: [18, 20, 22, 24, 26, 28, 30, 32]
  EB-SRT-1: [34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54]
  EB-SRT-2: [46, 48, 50, 52, 54]
---

# Hasil Search, Sort, dan Filter daftar akun

## Prerequisites
- Aktor: Admin A (DU-158-1), Total Control dengan cakupan seluruh client.
- Data:
  - DU-158-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-158-2: Account Code `SFA-{runId}`, Account Name `anggur Kas Saring {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0, Last Used in Journal kosong.
  - DU-158-3: Account Code `SFB-{runId}`, Account Name `Apel Kas Saring {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 2, Last Used in Journal `Sep 2025`.
  - DU-158-4: Account Code `SFC-{runId}`, Account Name `Beban Kas Saring {runId}`, Account Function `Accumulated Depreciation`, Status `Inactive`, Used By 0, Last Used in Journal `Jan 2026`.
  - DU-158-5: Account Code `SFD-{runId}`, Account Name `cabang Kas Saring {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 10, Last Used in Journal `Mar 2026`.
  - DU-158-6: Account Code `SFE-{runId}`, Account Name `Dana Kas Saring {runId}`, Account Function `Gain on Disposal`, Status `Inactive`, Used By 0, Last Used in Journal kosong.
  - DU-158-7: Account Code `SFF-{runId}`, Account Name `Kas Apel Lain Saring {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 1, Last Used in Journal kosong.
- Kondisi:
  - Akun dengan Used By lebih dari 0 dipakai oleh Asset Class sebanyak nilai Used By-nya; akun dengan Last Used in Journal terisi sudah pernah diekspor pada periode itu.
  - Pada permintaan daftar, `Saring {runId}` membatasi hasil ke keenam akun spec ini sehingga akun lain di client tidak memengaruhi urutan atau isi hasil; langkah yang tidak memakainya menyatakan sendiri akun yang dicek.

## Test Steps

### Search mencocokkan substring tanpa membedakan huruf besar atau kecil
1. Admin A mengirim permintaan daftar dengan Search `pel Kas Saring {runId}`, potongan yang dimulai di tengah kata
2. Verifikasi hasil memuat akun `SFB-{runId}` dan tidak memuat akun SF lain
3. Admin A mengirim permintaan daftar dengan Search `APEL KAS SARING {runId}`, huruf besar semua kecuali runId
4. Verifikasi hasil memuat akun `SFB-{runId}` dan tidak memuat akun SF lain, sama dengan pencarian huruf campuran
5. Admin A mengirim permintaan daftar dengan Search `sfc-{runId}`, huruf kecil atas Account Code
6. Verifikasi hasil memuat akun `SFC-{runId}` dan tidak memuat akun SF lain, karena kolom Account Code ikut dicari
7. Admin A mengirim permintaan daftar dengan Search `Accumulated Depreciation`, label badge kolom Function
8. Verifikasi hasil memuat akun `SFC-{runId}` dan tidak memuat akun `SFA-{runId}`, `SFB-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`, karena kolom Function ikut dicari
9. Admin A mengirim permintaan daftar dengan Search `Apel Lain Saring {runId}`, urutan kata yang sama dengan Account Name
10. Verifikasi hasil memuat akun `SFF-{runId}` dan tidak memuat akun SF lain, karena spasi di tengah query menjadi bagian dari teks yang dicari
11. Admin A mengirim permintaan daftar dengan Search `Lain Apel Saring {runId}`, kata yang sama dengan urutan terbalik
12. Verifikasi hasil kosong, karena query tidak dipecah menjadi kata-kata terpisah
13. Admin A mengirim permintaan daftar dengan Search `Mar 2026`, periode kolom Last Used in Journal akun `SFD-{runId}`
14. Verifikasi hasil tidak memuat akun `SFD-{runId}`, karena kolom Last Used in Journal dikecualikan dari Search
15. Admin A mengirim permintaan daftar dengan Search `Tidak Ada Saring {runId}` yang tidak cocok dengan akun mana pun
16. Verifikasi hasil kosong, yang pada tabel ditampilkan sebagai `No results found`

### Filter: logika OR dalam satu field dan AND antar field
17. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Function berisi `Asset Cost` dan `Gain on Disposal`
18. Verifikasi hasil memuat tepat akun `SFA-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`, gabungan (OR) dari kedua nilai dalam satu field
19. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Function berisi `Asset Cost` serta Filter Used By Min `1`
20. Verifikasi hasil memuat tepat akun `SFD-{runId}`, `SFF-{runId}`, irisan (AND) antar field, dan tidak memuat akun `SFA-{runId}` yang Used By-nya 0
21. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Active berisi `Active` dan `Inactive`
22. Verifikasi hasil memuat keenam akun `SFA-{runId}`, `SFB-{runId}`, `SFC-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`, gabungan (OR) kedua status
23. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Active berisi `Inactive`
24. Verifikasi hasil memuat tepat akun `SFC-{runId}`, `SFE-{runId}`
25. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Used By Min `2` serta Max `10`
26. Verifikasi hasil memuat tepat akun `SFB-{runId}`, `SFD-{runId}`, dengan kedua batas ikut (inklusif)
27. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Filter Last Used in Journal dari `Jan 2026` sampai `Mar 2026`
28. Verifikasi hasil memuat tepat akun `SFC-{runId}`, `SFD-{runId}`, dengan kedua bulan ikut (inklusif), dan tidak memuat akun `SFA-{runId}`, `SFE-{runId}`, `SFF-{runId}` yang Last Used in Journal-nya kosong
29. Admin A mengirim permintaan daftar dengan Search `Apel Kas Saring {runId}` dan Filter Function berisi `Asset Cost`
30. Verifikasi hasil kosong, karena akun yang cocok dengan Search (`SFB-{runId}`) tidak memenuhi Filter Function
31. Admin A mengirim permintaan daftar dengan Search `Apel` dan Filter Function berisi `Depreciation Expense`
32. Verifikasi hasil memuat akun `SFB-{runId}` dan tidak memuat akun `SFF-{runId}`, irisan Search dan Filter

### Sort sesuai tipe data kolom
33. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` tanpa Sort aktif
34. Verifikasi baris berurutan menurut default Account Code A-Z: `SFA-{runId}`, `SFB-{runId}`, `SFC-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`
35. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Account Name menaik
36. Verifikasi baris berurutan tanpa membedakan huruf besar atau kecil, sehingga Account Name `anggur Kas Saring {runId}` mendahului `Apel Kas Saring {runId}`: `SFA-{runId}`, `SFB-{runId}`, `SFC-{runId}`, `SFD-{runId}`, `SFE-{runId}`, `SFF-{runId}`
37. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Account Name menurun
38. Verifikasi baris berurutan `SFF-{runId}`, `SFE-{runId}`, `SFD-{runId}`, `SFC-{runId}`, `SFB-{runId}`, `SFA-{runId}`
39. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Function menaik
40. Verifikasi baris berurutan menurut label badge A-Z, dengan akun berfungsi sama diurutkan menurut default sort: `SFC-{runId}`, `SFA-{runId}`, `SFD-{runId}`, `SFF-{runId}`, `SFB-{runId}`, `SFE-{runId}`
41. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Active menaik (Active First)
42. Verifikasi akun Active di atas akun Inactive, masing-masing kelompok menurut default sort: `SFA-{runId}`, `SFB-{runId}`, `SFD-{runId}`, `SFF-{runId}`, `SFC-{runId}`, `SFE-{runId}`
43. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Active menurun (Inactive First)
44. Verifikasi akun Inactive di atas akun Active, masing-masing kelompok menurut default sort: `SFC-{runId}`, `SFE-{runId}`, `SFA-{runId}`, `SFB-{runId}`, `SFD-{runId}`, `SFF-{runId}`
45. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Used By menaik
46. Verifikasi baris berurutan menurut nilai angka natural (0, 0, 0, 1, 2, 10, bukan 0, 0, 0, 1, 10, 2), dengan akun ber-Used By sama menurut default sort: `SFA-{runId}`, `SFC-{runId}`, `SFE-{runId}`, `SFF-{runId}`, `SFB-{runId}`, `SFD-{runId}`
47. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Used By menurun
48. Verifikasi baris berurutan `SFD-{runId}`, `SFB-{runId}`, `SFF-{runId}`, `SFA-{runId}`, `SFC-{runId}`, `SFE-{runId}`, dengan akun ber-Used By sama tetap menurut default sort

### Sort dengan nilai kosong dan nilai sama
49. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Last Used in Journal menaik (Oldest First)
50. Verifikasi periode terlama di atas dan akun dengan Last Used in Journal kosong di akhir, akun kosong menurut default sort: `SFB-{runId}`, `SFC-{runId}`, `SFD-{runId}`, `SFA-{runId}`, `SFE-{runId}`, `SFF-{runId}`
51. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Last Used in Journal menurun (Newest First)
52. Verifikasi akun dengan Last Used in Journal kosong di awal, lalu periode terbaru ke terlama: `SFA-{runId}`, `SFE-{runId}`, `SFF-{runId}`, `SFD-{runId}`, `SFC-{runId}`, `SFB-{runId}`
53. Admin A mengirim permintaan daftar dengan Search `Saring {runId}` dan Sort Account Code menurun
54. Verifikasi baris berurutan `SFF-{runId}`, `SFE-{runId}`, `SFD-{runId}`, `SFC-{runId}`, `SFB-{runId}`, `SFA-{runId}`, dan urutan yang sama muncul pada permintaan ulang
