---
id: TC-AC-ACC-E2E-148-bulk-unsuspend-state-berubah-oleh-pelaku-lain
title: "Unsuspend: Sebagian atau Semua Client Terpilih Sudah di-Unsuspend dan Client Dihapus oleh Pelaku Lain Sebelum Confirm"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-461
  - TC-AC-ACC-462
  - TC-AC-ACC-646
coverage:
  web: automated
---

# Unsuspend: Sebagian atau Semua Client Terpilih Sudah di-Unsuspend dan Client Dihapus oleh Pelaku Lain Sebelum Confirm

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi UI yang diasersi): Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Pelaku kedua (Sesi B; hanya memicu perubahan state dan hasilnya di sesi itu tidak diasersi, sehingga memakai sesi API, bukan konteks UI kedua dan tidak memakai `P-2`): Active-Full A-15 yang sama (`AC_CLIENT_ACTIVE_FULL_PASSWORD`) lewat sesi API; sesi API aktor tidak dihitung sebagai sesi web; kemampuan ini disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data Pre-setup yang diubah lalu dipulihkan lewat UI (S-06): C-03 `PT Wahana Nusantara` (Suspended) dan C-LIF-6 `PT Ditahan Dua` (Suspended, FAMS Active; Tabel A3) di-Unsuspend lalu di-Suspend kembali. Efek: baris Changelog `Unsuspend`/`Suspend` dan Last Updated bertambah. C-LIF-21 `PT Uji Konkurensi 03` (Suspended; Tabel A3, kelas Dikonsumsi; dihapus oleh pelaku kedua, di-seed ulang tanpa syarat oleh Fixture BE yang disediakan tim FE/BE di hook `before` dan `after`).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-461: Bulk Unsuspend ketika sebagian Client terpilih sudah di-Unsuspend sesi lain: yang sudah Active di-skip dengan toast ringkasan T-27

1. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Wahana Nusantara` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Unsuspend` (N1)
2. [Sesi A] Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter, catat jumlah baris Action `Unsuspend` (N2), lalu tutup modal
3. [Sesi A] Klik sub-tab Suspended, ketik Search `PT Wahana Nusantara`, tekan Enter
4. [Sesi A] Centang baris `PT Wahana Nusantara`
5. [Sesi A] Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter, lalu centang baris `PT Ditahan Dua`
6. [Sesi A] Klik Bulk Action → pilih `Unsuspend` sampai dialog "Unsuspend Clients" terbuka
7. [Sesi A] Verifikasi dialog Title "Unsuspend Clients" dengan bullet `• PT Wahana Nusantara` dan `• PT Ditahan Dua`
8. [Sesi A] Verifikasi dialog memuat "Unsuspending these clients will restore access to all subscribed products. Are you sure you want to unsuspend them?"
9. [Sesi A] Verifikasi dialog memuat tombol `[Cancel]` dan `[Unsuspend]`
10. Unsuspend `PT Wahana Nusantara` lewat sesi API pelaku kedua hingga status Active tersimpan
11. [Sesi A] Klik `[Unsuspend]` pada dialog
12. [Sesi A] Verifikasi toast "Success, client has been unsuspended. Some items were skipped."
13. [Sesi A] Verifikasi tidak ada dialog blok
14. [Sesi A] Verifikasi Bulk Action Bar hilang
15. [Sesi A] Verifikasi seleksi di-reset ke 0 (tidak ada baris tercentang)
16. [Sesi A] Klik sub-tab Active, ketik Search `PT Ditahan Dua`, tekan Enter
17. [Sesi A] Verifikasi baris `PT Ditahan Dua` tampil di sub-tab Active
18. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Wahana Nusantara` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Unsuspend` (N3)
19. [Sesi A] Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter dan catat jumlah baris Action `Unsuspend` (N4)
20. [Sesi A] Verifikasi N3 adalah N1 + 1 (satu baris `Unsuspend` dari pelaku kedua; Sesi A tidak menambah baris untuk "PT Wahana Nusantara")
21. [Sesi A] Verifikasi N4 adalah N2 + 1 (satu baris `Unsuspend` dari Sesi A)
22. [Sesi A] Tutup modal Changelog, lalu Suspend ulang `PT Wahana Nusantara` dan `PT Ditahan Dua` (sub-tab Active, centang keduanya, Bulk Action → `Suspend`, `[Suspend]`)

### TC-AC-ACC-462: Bulk Unsuspend ketika semua Client terpilih sudah di-Unsuspend sesi lain: dialog blok D-16 tanpa toast sukses

23. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Wahana Nusantara` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Unsuspend` (N1)
24. [Sesi A] Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter, catat jumlah baris Action `Unsuspend` (N2), lalu tutup modal
25. [Sesi A] Klik sub-tab Suspended
26. [Sesi A] Ketik Search `PT Wahana Nusantara`, tekan Enter, lalu centang barisnya
27. [Sesi A] Ganti isi Search dengan `PT Ditahan Dua`, tekan Enter, lalu centang barisnya
28. [Sesi A] Klik Bulk Action → pilih `Unsuspend` sampai dialog "Unsuspend Clients" terbuka
29. Unsuspend `PT Wahana Nusantara` dan `PT Ditahan Dua` lewat sesi API pelaku kedua hingga keduanya Active tersimpan
30. [Sesi A] Klik `[Unsuspend]` pada dialog
31. [Sesi A] Verifikasi dialog blok Title "Unable to Unsuspend Clients" dengan bullet `• PT Wahana Nusantara` dan `• PT Ditahan Dua`
32. [Sesi A] Verifikasi dialog blok memuat "The selected clients cannot be unsuspended because they are already active or are derived clients."
33. [Sesi A] Verifikasi dialog blok memuat tombol `[OK]` dengan lebar 480px
34. [Sesi A] Verifikasi Sesi A tidak menampilkan toast sukses
35. [Sesi A] Klik `[OK]`
36. [Sesi A] Verifikasi kedua baris tetap tercentang
37. [Sesi A] Verifikasi Bulk Action Bar tetap tampil dengan jumlah terpilih 2 (seleksi dipertahankan setelah dialog blok D-16)
38. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Wahana Nusantara` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Unsuspend` (N3)
39. [Sesi A] Ganti isi Search modal dengan `PT Ditahan Dua` lalu tekan Enter dan catat jumlah baris Action `Unsuspend` (N4)
40. [Sesi A] Verifikasi N3 adalah N1 + 1 dan N4 adalah N2 + 1 (satu baris `Unsuspend` per Client dari pelaku kedua; Sesi A tidak menambah baris)
41. [Sesi A] Tutup modal Changelog, klik ikon (X) pada Bulk Action Bar, lalu Suspend ulang `PT Wahana Nusantara` dan `PT Ditahan Dua` (sub-tab Active, centang keduanya, Bulk Action → `Suspend`, `[Suspend]`)

### TC-AC-ACC-646: Unsuspend Client yang baru dihapus admin lain: toast netral dan kembali ke List

42. [Sesi A] Klik sub-tab Suspended, ketik Search `PT Uji Konkurensi 03`, tekan Enter
43. [Sesi A] Klik `[⋯]` pada baris `PT Uji Konkurensi 03` → pilih `Unsuspend` sampai dialog "Unsuspend Client" terbuka
44. Hapus Client `PT Uji Konkurensi 03` (nama konfirmasi persis) lewat sesi API pelaku kedua hingga Client terhapus
45. [Sesi A] Klik `[Unsuspend]` pada dialog
46. [Sesi A] Verifikasi toast netral "This client is no longer available."
47. [Sesi A] Verifikasi toast error "Error, failed to unsuspend client." tidak tampil
48. [Sesi A] Ketik Search `PT Uji Konkurensi 03`, tekan Enter
49. [Sesi A] Verifikasi List sub-tab Suspended disegarkan dan baris `PT Uji Konkurensi 03` tidak tampil
50. [Sesi A] Klik sub-tab Active, ketik Search `PT Uji Konkurensi 03`, tekan Enter
51. [Sesi A] Verifikasi sub-tab Active tidak memuat `PT Uji Konkurensi 03`

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Awalan `[Sesi A]` menandai sesi UI yang diasersi; langkah pelaku kedua tanpa awalan memakai sesi API.
- Pelaku kedua memakai sesi API karena hasilnya di sesi itu tidak diasersi (konvensi bagian 3 prinsip 13, keputusan 2026-10-30); langkah pemicu ditulis "... hingga ... tersimpan" (R-20). TC asal menyebut sesi kedua UI dan label "Manual Only: dua sesi paralel".
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas tiga TC satu topik (state berubah oleh pelaku lain sebelum konfirmasi Unsuspend); tiap blok menulis baseline sendiri dan memulihkan status Client-nya sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): pemulihan Bulk Suspend (langkah 22 dan 41), penutupan modal Changelog, klik ikon (X) pada Bulk Action Bar, dan Search yang menemukan baris target (R-16). Asersi absence baris `PT Uji Konkurensi 03` (langkah 49 dan 51) berlandaskan toast netral hasil server yang sudah diasersi (langkah 46) sebagai anchor positif (bagian 8b butir 2).
- Post Condition TC-AC-ACC-461 dan 462 ("Suspend ulang ...") sudah menjadi langkah; TC-AC-ACC-646 ("Seed ulang C-LIF-21") dilakukan di hook.
- Temuan untuk QA:
  - TC-AC-ACC-462 Expected a mengacu "Setelah langkah 11 (sebelum klik [OK] pada langkah 12)" pada nomor langkah TC; spec mengurutkan Verifikasi dialog blok sebelum `[OK]`.
  - TC-AC-ACC-462 langkah 10 ("Ulangi untuk PT Ditahan Dua") disalin sebagai satu langkah pelaku kedua untuk kedua Client.
