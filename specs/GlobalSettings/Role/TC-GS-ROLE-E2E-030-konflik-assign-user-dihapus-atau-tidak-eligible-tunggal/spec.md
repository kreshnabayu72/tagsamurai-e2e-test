---
id: TC-GS-ROLE-E2E-030-konflik-assign-user-dihapus-atau-tidak-eligible-tunggal
title: "Konflik Assign: User Terpilih Dihapus atau Tidak Eligible Sebelum Submit (Alert Tunggal)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-65
  - TC-GS-ROLE-66
  - TC-GS-ROLE-67
  - TC-GS-ROLE-83
  - TC-GS-ROLE-292
coverage:
  web: automated
---

# Konflik Assign: User Terpilih Dihapus atau Tidak Eligible Sebelum Submit (Alert Tunggal)

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (c), dua admin; objek uji adalah perilaku sesi A setelah admin kedua mengubah state.
- Akun aktor sesi A (hook `before`): Ahmad Fauzi (Total Control), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Admin kedua: Eko Prasetyo (Total Control, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Eko hanya memicu perubahan state lewat sesi API (tanpa sesi UI kedua).
- Layar awal (hook `beforeEach`): Global Settings > Role & Permission > Tab Total Control.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (`suite.md`).
- Data Pre-setup yang dipakai (bukan data baru sehingga tanpa suffix `+{runId}-030`; diubah dan dipulihkan sesuai catatan "Reset Pre-setup per TC" dan Tabel Dinamis #6 di `tc-role.md`):
  - Nina Kartika dan Wawan Setiawan (Pre-setup #11, Active): state kandidat, yaitu Access Global Settings dicentang, tanpa access level, dan tanpa baris role. Wawan Setiawan dihapus atau diubah sesi API Eko di TC-GS-ROLE-65, 66, 83, dan 292; Nina Kartika di-assign Total Control oleh sesi API Eko di TC-GS-ROLE-83 dan oleh sesi A di TC-GS-ROLE-65.
  - Olivia Rahma (Pre-setup #18, Active, Access Global Settings dicentang, tanpa access level, tanpa baris role) untuk TC-GS-ROLE-67; di-rename sesi API Eko menjadi Olivia Rahmawati dan menjadi Total Control (Tabel Dinamis #11).
  - Hendra Wijaya (Pre-setup #5) dipakai hanya sebagai baris pembanding di picker Tab Read Only (tanpa access level); tidak diubah.
- Pemulihan: antar TC dikembalikan lewat langkah penghubung sesi API Eko (langkah 11, 28, 49, 71) dan sebagai cadangan di hook `after`: Nina Kartika dan Wawan Setiawan ke state kandidat (dibuat ulang bila dihapus), Olivia Rahma ke nama awal tanpa access level dan tanpa baris role.
- Efek pemulihan yang tidak dikembalikan: perubahan dan pemulihan sesi API Eko meninggalkan efek pada Modified By, Last Updated, dan entri Changelog user kandidat (Nina Kartika, Wawan Setiawan, Olivia Rahma) yang tidak dapat dipulihkan. Spec tidak mengasersi Modified By dan Last Updated user tersebut; asersi jumlah entry Changelog (langkah 13 dan 26) memakai baseline yang dicatat sebelum aksi (S-12).
- Kemampuan teknis (disediakan tim FE/BE; nama endpoint tidak ditentukan di TC, PRD, dan LLD): klien HTTP terotentikasi sebagai Eko Prasetyo untuk: menghapus user, menghapus centang Access Global Settings user, meng-assign Total Control, me-rename user, mencabut access level, dan membuat ulang user kandidat; membaca nilai total baris dari info pagination dan jumlah entry Modal Changelog dari UI.

## Test Steps

### TC-GS-ROLE-292: Assign Total Control saat Access Global Settings user terpilih dicabut sebelum submit

1. Klik `[+ Assign]`
2. Centang Nina Kartika dan Wawan Setiawan
3. Sesi API Eko: hapus centang Access Global Settings pada user Wawan Setiawan di modul User hingga perubahan Access Global Settings tersimpan
4. Klik `[Assign]`
5. Verifikasi alert inline (danger) `Wawan Setiawan is no longer eligible. Please select another.` tampil
6. Verifikasi Nina Kartika tetap tercentang
7. Verifikasi counter `1 user selected` tampil (hanya centangan Wawan Setiawan yang hilang)
8. Verifikasi Nina Kartika tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
9. Verifikasi Wawan Setiawan tidak tampil di picker setelah picker di-refetch
10. Klik `[Cancel]`
11. Sesi API Eko: centang kembali Access Global Settings pada user Wawan Setiawan hingga perubahan Access Global Settings tersimpan

### TC-GS-ROLE-66: Assign Total Control saat user terpilih menjadi tidak eligible sebelum submit

12. Buka Modal Changelog Tab Total Control
13. Catat jumlah entry Assign dengan Modified By `Ahmad F` untuk Nina Kartika dan Wawan Setiawan sebagai baseline
14. Tutup Modal Changelog
15. Klik `[+ Assign]`
16. Centang Nina Kartika dan Wawan Setiawan
17. Sesi API Eko: assign Total Control ke Wawan Setiawan hingga access level Total Control Wawan Setiawan tersimpan
18. Klik `[Assign]`
19. Verifikasi alert inline (danger) `Wawan Setiawan is no longer eligible. Please select another.` tampil
20. Verifikasi Nina Kartika tetap tercentang
21. Verifikasi counter `1 user selected` tampil (hanya centangan Wawan Setiawan yang hilang)
22. Verifikasi Nina Kartika tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
23. Verifikasi Wawan Setiawan tidak tampil di picker setelah picker di-refetch
24. Klik `[Cancel]`
25. Buka Modal Changelog Tab Total Control
26. Verifikasi jumlah entry Assign dengan Modified By `Ahmad F` untuk Nina Kartika dan Wawan Setiawan sama dengan baseline pada langkah 13
27. Tutup Modal Changelog
28. Sesi API Eko: cabut access level Total Control dari Wawan Setiawan hingga pencabutan access level tersimpan

### TC-GS-ROLE-67: Assign Total Control saat user terpilih di-rename sebelum submit

29. Klik `[+ Assign]`
30. Centang Olivia Rahma
31. Sesi API Eko: rename Olivia Rahma menjadi Olivia Rahmawati di modul User hingga nama Olivia Rahmawati tersimpan
32. Klik `[Assign]`
33. Verifikasi toast sukses `Success, Total Control has been assigned.` tampil
34. Verifikasi tidak ada alert stale reference yang tampil
35. Verifikasi baris `Olivia Rahmawati` tampil di Tab Total Control

### TC-GS-ROLE-65: Assign Total Control saat user terpilih dihapus admin lain sebelum submit

36. Klik `[+ Assign]`
37. Centang Nina Kartika dan Wawan Setiawan
38. Sesi API Eko: hapus user Wawan Setiawan di modul User hingga penghapusan tersimpan
39. Klik `[Assign]`
40. Verifikasi alert inline (danger) `Wawan Setiawan no longer exists. Please select another.` tampil
41. Verifikasi popup Assign Total Control tetap terbuka
42. Verifikasi Nina Kartika tetap tercentang
43. Verifikasi counter `1 user selected` tampil (hanya centangan Wawan Setiawan yang hilang)
44. Verifikasi Nina Kartika tetap tampil di picker, artinya belum menjadi Total Control (submit ditolak seluruhnya)
45. Verifikasi Wawan Setiawan tidak tampil di picker setelah picker di-refetch
46. Klik `[Assign]` ulang
47. Verifikasi toast sukses `Success, Total Control has been assigned.` tampil
48. Verifikasi baris Nina Kartika tampil di Tab Total Control
49. Sesi API Eko: cabut access level Total Control dari Nina Kartika dan buat ulang user Wawan Setiawan sebagai kandidat hingga pencabutan access level dan user kandidat tersimpan

### TC-GS-ROLE-83: Assign Read Only saat user terpilih dihapus atau menjadi tidak eligible sebelum submit

50. Buka Tab Read Only
51. Catat total baris Tab Read Only dari info pagination sebagai baseline
52. Klik `[+ Assign]`
53. Centang Wawan Setiawan dan Nina Kartika
54. Sesi API Eko: assign Total Control ke Nina Kartika hingga access level Total Control Nina Kartika tersimpan
55. Klik `[Assign]`
56. Verifikasi alert inline `Nina Kartika is no longer eligible. Please select another.` tampil
57. Verifikasi Wawan Setiawan tetap tercentang
58. Verifikasi counter `1 user selected` tampil (hanya centangan Nina Kartika yang hilang)
59. Verifikasi Wawan Setiawan tetap tampil di picker, artinya belum menjadi Read Only (submit atomik)
60. Verifikasi Nina Kartika tidak tampil di picker setelah picker di-refetch
61. Sesi API Eko: hapus user Wawan Setiawan di modul User hingga penghapusan tersimpan
62. Klik `[Assign]` lagi
63. Verifikasi alert inline `Wawan Setiawan no longer exists. Please select another.` tampil
64. Ketik Search `Hendra Wijaya` di picker, tekan Enter
65. Verifikasi baris Hendra Wijaya tampil di picker
66. Verifikasi tidak ada user tercentang di picker (centangan Wawan Setiawan hilang)
67. Ketik Search `Wawan Setiawan` di picker, tekan Enter
68. Verifikasi Wawan Setiawan tidak tampil di picker setelah picker di-refetch
69. Klik `[Cancel]`
70. Verifikasi total baris Tab Read Only sama dengan baseline pada langkah 51 (tidak ada user yang menjadi Read Only)
71. Sesi API Eko: cabut access level Total Control dari Nina Kartika dan buat ulang user Wawan Setiawan sebagai kandidat hingga pencabutan access level dan user kandidat tersimpan

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (c), dua admin, satu spec untuk satu jenis harness.
- `P-1`: asersi jumlah entry Changelog pada TC-GS-ROLE-66 (langkah 26: "tidak ada entry Assign baru dari sesi A") bergantung pada state yang baru dibangun langkah sebelumnya di spec ini (perubahan sesi API Eko dan penolakan submit sesi A); ditulis sebagai `Verifikasi` berbaseline (langkah 13) karena tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (69 langkah). Alasan: lima TC satu kelas harness (konflik antar admin dengan Eko via API) dan satu layar (popup Assign Total Control/Read Only); tiap blok berdiri sendiri karena data dipulihkan oleh langkah penghubung sesi API Eko di antara blok, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC yang menghapus user (TC-GS-ROLE-65 dan TC-GS-ROLE-83) diletakkan paling akhir.
- Urutan TC sumber diubah (292, 66, 67, 65, 83) agar blok yang menghapus user berada di akhir dan blok Tab Read Only berada terakhir (bagian 3 prinsip 5).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik `[Cancel]` menutup popup (langkah 10, 24, 69), pemulihan sesi API Eko (langkah 11, 28, 49, 71), pencatatan baseline dan membuka atau menutup Modal Changelog (langkah 12 sampai 14, 25, 27, 51), serta membuka Tab Read Only (langkah 50).
- Asersi tambahan di luar kalimat Expected TC (dicatat sesuai S-03): "Nina Kartika tetap tampil di picker" (langkah 8, 22, 44) dan "Wawan Setiawan tetap tampil di picker" (langkah 59) membuktikan Expected "submit ditolak seluruhnya, user terpilih tidak menjadi Total Control/Read Only" karena pool picker hanya memuat user tanpa access level yang sesuai; "baris Hendra Wijaya tampil di picker" (langkah 65) dan "Nina Kartika tetap tercentang" menjadi anchor positif bagi asersi absence di picker (bagian 8b butir 2).
- Expected TC-GS-ROLE-65 b diamati lewat pool picker (langkah 44) dan bukan lewat Tab Total Control, karena popup harus tetap terbuka untuk `[Assign]` ulang (langkah 46).
- Expected TC-GS-ROLE-83 b (Wawan Setiawan tidak menjadi Read Only) dan d (tidak ada user yang menjadi Read Only) diamati lewat pool picker (langkah 59) dan total baris Tab Read Only (langkah 70).
- Langkah penghubung (R-16, bukan dari TC sumber): Search `Hendra Wijaya` (langkah 64) sebelum `Verifikasi` baris pembanding karena picker berpagination; Search `Wawan Setiawan` (langkah 67) mengganti isinya sebelum absence langkah 68, dengan anchor positif baris Hendra Wijaya pada langkah 65.
- Temuan untuk QA:
  - TC-GS-ROLE-65, 66, 83, dan 292 menyebut "centang" dan "hapus" tanpa cara menemukan baris bila picker lebih dari satu halaman; spec mengikuti TC dan mekanisme menemukan baris diputuskan di tahap script.
  - Counter seleksi `1 user selected` (langkah 7, 21, 43, 58) diturunkan dari "hanya centangan <nama> yang hilang" memakai teks counter TC-GS-ROLE-55; TC-GS-ROLE-65, 66, 83, dan 292 tidak menyebut teks counter.
  - TC-GS-ROLE-66 d tidak menyebut kolom Changelog yang menandai sesi A; spec memakai Modified By `Ahmad F`, formatnya mengikuti Expected TC-GS-ROLE-58 b.
  - TC-GS-ROLE-67 tidak menyebut cara memulihkan nama Olivia Rahma dan Tabel Dinamis #11 menyatakan tetap Total Control; spec memulihkannya di hook `after` agar dapat diulang.
  - TC-GS-ROLE-83 Expected d menyebut "tidak ada user yang menjadi Read Only" tanpa nilai pembanding; spec memakai baseline total baris Tab Read Only (langkah 51).
