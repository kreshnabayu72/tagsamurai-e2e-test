---
id: TC-FA-TDC-E2E-280-create-helper-equivalent-declining-balance-rate-faktor-pembulatan-hitung-ulang-dan-tidak-valid
title: "Drawer Create: Helper Equivalent Declining Balance Rate (Faktor, Pembulatan Half-Up, Hitung Ulang Seketika, dan Keadaan Tidak Valid)"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-939
  - TC-FA-TDC-940
  - TC-FA-TDC-941
  - TC-FA-TDC-942
sourceRules: ["FLD-08", "FI-12", "FATDC-LOGIC-03f.6", "V-12", "V-17"]
smoke: []
dependsOn: []
trace:
  "FLD-08": [6, 9, 12, 13, 14, 15]
  "FI-12": [6, 9, 12, 18, 20, 23, 26, 29, 31, 33, 36, 38, 42, 46, 49, 53]
  "FATDC-LOGIC-03f.6": [6, 9, 12, 13, 18, 20, 23, 26, 29, 31, 33, 36, 38, 41, 42, 45, 46, 49, 53]
  "V-12": [52]
  "V-17": [48]
coverage:
  web: automated
---

# Drawer Create: Helper Equivalent Declining Balance Rate (Faktor, Pembulatan Half-Up, Hitung Ulang Seketika, dan Keadaan Tidak Valid)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Master Data Count Limit belum tercapai (Precondition c keempat TC); kemampuan mengatur kuota disediakan tim FE/BE.
- Spec tidak membuat data, tidak mengubah data, dan tidak mengubah state global; form Create tidak pernah di-Submit.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-939: Helper menampilkan padanan faktor terhadap Straight Line Rate

1. Klik `+ Class` di toolbar
2. Pilih Asset Type `Non-building`
3. Pilih Allowed Methods `Declining Balance`
4. Isi Useful Life `4`
5. Isi Declining Balance Rate `50`
6. Verifikasi helper "Equivalent to 2.0× the straight-line rate"
7. Ganti Useful Life menjadi `15`
8. Ganti Declining Balance Rate menjadi `10`
9. Verifikasi helper "Equivalent to 1.5× the straight-line rate"
10. Ganti Useful Life menjadi `8`
11. Ganti Declining Balance Rate menjadi `25`
12. Verifikasi helper "Equivalent to 2.0× the straight-line rate"
13. Verifikasi helper tampil sebagai teks informasi di bawah input Declining Balance Rate (%)
14. Verifikasi nilai Declining Balance Rate (%) tetap "25"
15. Verifikasi input Declining Balance Rate (%) masih dapat diedit (helper tidak mengunci atau mengubah nilai)

### TC-FA-TDC-940: Helper dibulatkan half-up ke 1 desimal dari 100 ÷ Useful Life tanpa pembulatan

16. Ganti Useful Life menjadi `10`
17. Ganti Declining Balance Rate menjadi `12.5`
18. Verifikasi helper "Equivalent to 1.3× the straight-line rate" (faktor 1.25)
19. Ganti Declining Balance Rate menjadi `13.5`
20. Verifikasi helper "Equivalent to 1.4× the straight-line rate" (faktor 1.35)
21. Ganti Useful Life menjadi `3`
22. Ganti Declining Balance Rate menjadi `66.67`
23. Verifikasi helper "Equivalent to 2.0× the straight-line rate" (faktor 2.0001)
24. Ganti Useful Life menjadi `6`
25. Ganti Declining Balance Rate menjadi `12.5`
26. Verifikasi helper "Equivalent to 0.8× the straight-line rate" (faktor 0.75)

### TC-FA-TDC-941: Helper dihitung ulang seketika saat Useful Life atau Declining Balance Rate berubah

27. Ganti Useful Life menjadi `8`
28. Ganti Declining Balance Rate menjadi `25`
29. Verifikasi helper "Equivalent to 2.0× the straight-line rate"
30. Ganti Useful Life menjadi `10`
31. Verifikasi helper "Equivalent to 2.5× the straight-line rate" seketika tanpa Submit
32. Ganti Declining Balance Rate menjadi `30`
33. Verifikasi helper "Equivalent to 3.0× the straight-line rate"
34. Hapus Useful Life
35. Verifikasi Declining Balance Rate tetap "30"
36. Verifikasi helper "Equivalent to ..." tidak tampil
37. Isi Useful Life `8`
38. Verifikasi helper "Equivalent to 2.4× the straight-line rate"

### TC-FA-TDC-942: Helper Equivalent tidak tampil dan helper bawaan tampil bila Useful Life atau Declining Balance Rate kosong atau tidak valid

39. Hapus Useful Life
40. Ganti Declining Balance Rate menjadi `25`
41. Verifikasi helper "Use the rate set by your country's tax regulation." tampil
42. Verifikasi helper "Equivalent to ..." tidak tampil
43. Isi Useful Life `8`
44. Kosongkan Declining Balance Rate
45. Verifikasi helper "Use the rate set by your country's tax regulation." tampil
46. Verifikasi helper "Equivalent to ..." tidak tampil
47. Isi Declining Balance Rate `150`
48. Verifikasi caption "Declining rate must be between 0 and 100" tampil
49. Verifikasi helper "Equivalent to ..." tidak tampil
50. Ganti Declining Balance Rate menjadi `25`
51. Ganti Useful Life menjadi `101`
52. Verifikasi caption "Useful life must be between 1 and 100 years" tampil pada Useful Life
53. Verifikasi helper "Equivalent to ..." tidak tampil
54. Klik `[×]` pada Drawer Create
55. Verifikasi dialog `Unsaved Changes` tampil
56. Klik `[Leave]`

## Notes

- Alasan melewati sekitar 35 langkah (56 langkah): keempat TC hanya mengetik dan mengamati helper pada form Create yang sama tanpa Submit, sehingga memakai satu pembukaan form dengan field diganti di antara kasus (halaman yang sama dipakai berulang, prinsip 3 bagian 3); semua blok satu topik dan berdiri sendiri.
- Urutan dan form: keempat TC berbagi form yang sama; langkah 1 sampai 3 membuka form dan memilih Non-building dan `Declining Balance` sekali (langkah 1 dan 2 TC-FA-TDC-940 sampai TC-FA-TDC-942 dipenuhi oleh keadaan form sebelumnya, dan tidak diulang karena memilih lagi `Declining Balance` akan melepasnya). Form ditutup di langkah 54 sampai 56 (S-08); tidak ada Submit.
- Langkah penghubung (S-03): langkah 7, 10, 16, 21, 24, 27, 30, 39, 43, dan 51 mengganti nilai tanpa `Verifikasi` (TC memakai "Ganti" atau "Isi"); langkah 54 sampai 56 (menutup form dirty).
- Asersi tambahan di luar Expected TC (S-03): langkah 35 (Declining Balance Rate tetap "30") adalah anchor positif untuk asersi absence langkah 36; urutannya ditukar dengan TC-FA-TDC-941 Expected d ("helper tidak tampil; Declining Balance Rate tetap "30"") karena asersi absence didahului anchor (8b.2). Langkah 41 dan 45 (helper bawaan tampil, Expected a dan b TC-FA-TDC-942) juga anchor untuk langkah 42 dan 46; langkah 48 dan 52 (caption tampil) anchor untuk langkah 49 dan 53.
- Langkah 18, 20, 23, dan 26 menuliskan faktor di kurung hanya sebagai keterangan perhitungan Expected TC-FA-TDC-940 (faktor = Declining Balance Rate ÷ (100 ÷ Useful Life)); asersinya hanya teks helper.
- Temuan untuk QA:
  - TC-FA-TDC-939 sampai 942 menyebut "Isi Useful Life ... dan Declining Balance Rate ..." dalam satu langkah tanpa urutan isian; spec mengisi Useful Life lebih dulu lalu Declining Balance Rate.
  - TC-FA-TDC-942 langkah 3 mengisi Declining Balance Rate `25` dengan Useful Life kosong; spec menghapus Useful Life (langkah 39) karena form lanjutan TC-FA-TDC-941 sudah berisi Useful Life.
  - TC-FA-TDC-942 Expected c dan d tidak menyebut helper bawaan; spec mengasersi hanya "Equivalent to ..." tidak tampil pada langkah 49 dan 53 sesuai TC.
  - TC-FA-TDC-939 sampai 942 Post Condition "Tidak ada data berubah" tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
