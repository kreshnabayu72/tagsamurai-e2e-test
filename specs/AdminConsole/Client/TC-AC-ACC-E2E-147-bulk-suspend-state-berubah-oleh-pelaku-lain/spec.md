---
id: TC-AC-ACC-E2E-147-bulk-suspend-state-berubah-oleh-pelaku-lain
title: "Suspend: Sebagian atau Semua Client Terpilih Sudah Disuspend dan Client Dihapus oleh Pelaku Lain Sebelum Confirm"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-211
  - TC-AC-ACC-643
  - TC-AC-ACC-645
coverage:
  web: automated
---

# Suspend: Sebagian atau Semua Client Terpilih Sudah Disuspend dan Client Dihapus oleh Pelaku Lain Sebelum Confirm

## Prerequisites

- Mode: FE+BE.
- Akun aktor (sesi UI yang diasersi): Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Pelaku kedua (Sesi B; hanya memicu perubahan state dan hasilnya di sesi itu tidak diasersi, sehingga memakai sesi API, bukan konteks UI kedua dan tidak memakai `P-2`): Active-Full A-15 yang sama (`AC_CLIENT_ACTIVE_FULL_PASSWORD`) lewat sesi API; sesi API aktor tidak dihitung sebagai sesi web (tidak mengusir sesi UI); kemampuan ini disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data Pre-setup yang diubah lalu dipulihkan lewat UI (S-06): C-11 `PT Sinar Distributor` dan C-13 `PT Ganti Mitra` (Active; di-Suspend lalu di-Unsuspend). Efek: baris Changelog `Suspend`/`Unsuspend` dan Last Updated bertambah. C-LIF-19 `PT Uji Konkurensi 01` (Tabel A3, kelas Dikonsumsi; dihapus oleh Sesi B, di-seed ulang tanpa syarat oleh Fixture BE yang disediakan tim FE/BE di hook `before` dan `after`).
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-211: Bulk Suspend ketika sebagian Client terpilih sudah di-Suspend sesi lain: yang sudah Suspended di-skip dengan toast ringkasan T-26

1. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Sinar Distributor` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Suspend` (N1)
2. [Sesi A] Ganti isi Search modal dengan `PT Ganti Mitra` lalu tekan Enter, catat jumlah baris Action `Suspend` (N2), lalu tutup modal
3. [Sesi A] Klik sub-tab Active lalu ketik Search `PT Sinar Distributor` dan tekan Enter
4. [Sesi A] Centang baris `PT Sinar Distributor`
5. [Sesi A] Ganti isi Search dengan `PT Ganti Mitra`, tekan Enter, lalu centang baris `PT Ganti Mitra`
6. [Sesi A] Klik Bulk Action → pilih `Suspend` sampai dialog "Suspend Clients" terbuka
7. [Sesi A] Verifikasi dialog Title "Suspend Clients" dengan bullet `• PT Sinar Distributor` dan `• PT Ganti Mitra`
8. [Sesi A] Verifikasi dialog memuat "Suspending these clients will make access to all subscribed products read-only. Subscription lifecycle will continue running in the background. Are you sure you want to suspend them?"
9. [Sesi A] Verifikasi dialog memuat tombol `[Cancel]` dan `[Suspend]`
10. Suspend `PT Sinar Distributor` lewat sesi API pelaku kedua hingga status Suspended tersimpan
11. [Sesi A] Klik `[Suspend]` pada dialog
12. [Sesi A] Verifikasi toast "Success, client has been suspended. Some items were skipped."
13. [Sesi A] Verifikasi tidak ada dialog blok
14. [Sesi A] Verifikasi Bulk Action Bar hilang
15. [Sesi A] Verifikasi seleksi di-reset ke 0 (tidak ada baris tercentang)
16. [Sesi A] Klik sub-tab Suspended, ketik Search `PT Sinar Distributor`, tekan Enter
17. [Sesi A] Verifikasi baris `PT Sinar Distributor` tampil di sub-tab Suspended
18. [Sesi A] Ganti isi Search dengan `PT Ganti Mitra`, tekan Enter
19. [Sesi A] Verifikasi baris `PT Ganti Mitra` tampil di sub-tab Suspended
20. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Sinar Distributor` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Suspend` (N3)
21. [Sesi A] Ganti isi Search modal dengan `PT Ganti Mitra` lalu tekan Enter dan catat jumlah baris Action `Suspend` (N4)
22. [Sesi A] Verifikasi N3 adalah N1 + 1 (satu baris `Suspend` dari pelaku kedua; Sesi A tidak menambah baris untuk "PT Sinar Distributor")
23. [Sesi A] Verifikasi N4 adalah N2 + 1 (satu baris `Suspend` dari Sesi A)
24. [Sesi A] Tutup modal Changelog, lalu Unsuspend `PT Sinar Distributor` dan `PT Ganti Mitra` (centang keduanya di sub-tab Suspended, Bulk Action → `Unsuspend`, `[Unsuspend]`)

### TC-AC-ACC-643: Bulk Suspend ketika semua Client terpilih sudah di-Suspend sesi lain: dialog blok D-15 tanpa toast sukses

25. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Sinar Distributor` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Suspend` (N1)
26. [Sesi A] Ganti isi Search modal dengan `PT Ganti Mitra` lalu tekan Enter, catat jumlah baris Action `Suspend` (N2), lalu tutup modal
27. [Sesi A] Klik sub-tab Active lalu ketik Search `PT Sinar Distributor` dan tekan Enter
28. [Sesi A] Centang baris `PT Sinar Distributor`
29. [Sesi A] Ganti isi Search dengan `PT Ganti Mitra`, tekan Enter, lalu centang baris `PT Ganti Mitra`
30. [Sesi A] Klik Bulk Action → pilih `Suspend` sampai dialog "Suspend Clients" terbuka
31. Suspend `PT Sinar Distributor` dan `PT Ganti Mitra` lewat sesi API pelaku kedua hingga keduanya Suspended tersimpan
32. [Sesi A] Klik `[Suspend]` pada dialog
33. [Sesi A] Verifikasi dialog blok Title "Unable to Suspend Clients" dengan bullet `• PT Sinar Distributor` dan `• PT Ganti Mitra`
34. [Sesi A] Verifikasi dialog blok memuat "The selected clients cannot be suspended because they are already suspended or are derived clients."
35. [Sesi A] Verifikasi dialog blok memuat tombol `[OK]` dengan lebar 480px
36. [Sesi A] Verifikasi Sesi A tidak menampilkan toast sukses
37. [Sesi A] Klik `[OK]`
38. [Sesi A] Verifikasi kedua baris tetap tercentang
39. [Sesi A] Verifikasi Bulk Action Bar tetap tampil dengan jumlah terpilih 2 (seleksi dipertahankan setelah dialog blok D-15)
40. [Sesi A] Klik `[Changelog]` di toolbar List, ketik `PT Sinar Distributor` di Search modal lalu tekan Enter, ubah ukuran halaman modal menjadi 100, lalu catat jumlah baris Action `Suspend` (N3)
41. [Sesi A] Ganti isi Search modal dengan `PT Ganti Mitra` lalu tekan Enter dan catat jumlah baris Action `Suspend` (N4)
42. [Sesi A] Verifikasi N3 adalah N1 + 1 dan N4 adalah N2 + 1 (satu baris `Suspend` per Client dari pelaku kedua; Sesi A tidak menambah baris)
43. [Sesi A] Tutup modal Changelog, klik ikon (X) pada Bulk Action Bar, lalu Unsuspend `PT Sinar Distributor` dan `PT Ganti Mitra` (sub-tab Suspended, centang keduanya, Bulk Action → `Unsuspend`, `[Unsuspend]`)

### TC-AC-ACC-645: Suspend Client yang baru dihapus admin lain: toast netral dan kembali ke List

44. [Sesi A] Klik sub-tab Active, ketik Search `PT Uji Konkurensi 01`, tekan Enter
45. [Sesi A] Klik `[⋯]` pada baris `PT Uji Konkurensi 01` → pilih `Suspend` sampai dialog "Suspend Client" terbuka
46. Hapus Client `PT Uji Konkurensi 01` (nama konfirmasi persis) lewat sesi API pelaku kedua hingga Client terhapus
47. [Sesi A] Klik `[Suspend]` pada dialog
48. [Sesi A] Verifikasi toast netral "This client is no longer available."
49. [Sesi A] Verifikasi toast error "Error, failed to suspend client." tidak tampil
50. [Sesi A] Ketik Search `PT Uji Konkurensi 01`, tekan Enter
51. [Sesi A] Verifikasi List sub-tab Active disegarkan dan baris `PT Uji Konkurensi 01` tidak tampil
52. [Sesi A] Klik sub-tab Suspended, ketik Search `PT Uji Konkurensi 01`, tekan Enter
53. [Sesi A] Verifikasi sub-tab Suspended tidak memuat `PT Uji Konkurensi 01`

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Awalan `[Sesi A]` menandai sesi UI yang diasersi; langkah pelaku kedua tanpa awalan memakai sesi API.
- Pelaku kedua memakai sesi API karena hasilnya di sesi itu tidak diasersi (konvensi bagian 3 prinsip 13, keputusan 2026-10-30); langkah pemicu ditulis "... hingga ... tersimpan" (R-20). TC asal menyebut sesi kedua UI dan label "Manual Only: dua sesi paralel".
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) dan baseline Changelog (S-12) atas tiga TC satu topik (state berubah oleh pelaku lain sebelum konfirmasi Suspend); tiap blok memakai Client dan baseline sendiri dan memulihkan statusnya sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): pemulihan Bulk Unsuspend (langkah 24 dan 43), penutupan modal Changelog, klik (X) pada Bulk Action Bar, dan Search yang menemukan baris target (R-16). Asersi absence baris `PT Uji Konkurensi 01` (langkah 51 dan 53) berlandaskan toast netral hasil server yang sudah diasersi (langkah 48) sebagai anchor positif (bagian 8b butir 2).
- Post Condition TC-AC-ACC-211 dan 643 ("Unsuspend ...") sudah menjadi langkah; TC-AC-ACC-645 ("Seed ulang C-LIF-19") dilakukan di hook.
- Temuan untuk QA:
  - TC-AC-ACC-643 Expected a mengacu "Setelah langkah 9 (sebelum klik [OK] pada langkah 12)" pada nomor langkah TC; spec mengurutkan Verifikasi dialog blok sebelum `[OK]`.
  - TC-AC-ACC-645 langkah 5 meminta pencarian di sub-tab Suspended setelah Client dihapus; hasil pencarian bergantung pada kemampuan sub-tab memuat data terkini.
