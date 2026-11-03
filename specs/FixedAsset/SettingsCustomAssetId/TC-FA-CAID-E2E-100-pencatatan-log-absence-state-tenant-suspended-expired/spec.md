---
id: TC-FA-CAID-E2E-100-pencatatan-log-absence-state-tenant-suspended-expired
title: "Pencatatan Log Absence: Save dan Toggle Ditolak Saat Entitas Suspended atau Expired Tanpa Entri Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-312
  - TC-FA-CAID-313
coverage:
  web: automated
---

# Pencatatan Log Absence: Save dan Toggle Ditolak Saat Entitas Suspended atau Expired Tanpa Entri Log

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini memakai akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`); spec tidak mengasersi apa pun di Company Alpha. Kedua entitas diuji lewat perulangan yang dimulai dengan langkah ganti akun eksplisit (langkah 1), bukan di hook `before`. Hook `after` spec ini mengembalikan sesi ke akun default suite. Halaman yang dibuka hook `beforeEach` suite tidak dipakai langkah.
- Role yang diuji (Total Control; email `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari env, tidak ditulis di spec atau fixture). Email akun tiap Company khusus tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun dan env var di tabel ini disediakan tim FE dan nama env adalah usulan yang perlu konfirmasi tim FE.

| Iterasi | Entitas (Pre-setup) | Env password |
|---|---|---|
| 1 | Client Suspended (No 20) | `Spectra.env.FA_SUSPENDED_TC_PASSWORD` |
| 2 | Client Expired (No 21) | `Spectra.env.FA_EXPIRED_TC_PASSWORD` |

- Data Pre-setup No 20 dan No 21: Client Suspended dan Client Expired masing-masing dengan Total Control, konfigurasi B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), dan aset A1 sampai A4 (Pre-setup No 11; Asset ID tidak berubah selama spec). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE). Seed company khusus dikembalikan tim FE/BE sebelum tiap run (`suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): pembacaan jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log aktor, dan Activity Log sebelum dan sesudah aksi (mekanisme tidak tertulis di TC, PRD, atau LLD; langkah 2 dan 23 memakai selisih terhadap baseline, S-12).
- Spec tidak membuat data dan tidak mengubah state global; penolakan tulis oleh server tidak mengubah konfigurasi. Entri log yang sudah ada tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

Untuk setiap entitas pada tabel Role yang diuji (Client Suspended, lalu Client Expired) lakukan langkah 1 sampai 40 (diulang dua kali):

1. Ganti akun: logout akun yang sedang login, login sebagai Total Control entitas pada baris tabel, lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-312: Save saat entitas Suspended atau Expired ditolak

2. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log aktor, dan Activity Log
3. Pilih Separator `- (Dash)`
4. Klik `[Save]`
5. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
6. Tutup toast error (dismiss)
7. Klik tombol `[Changelog]`
8. Verifikasi modal `Changelog: Custom Asset ID` terbuka dan menampilkan tabel riwayat
9. Verifikasi jumlah entri Changelog sama dengan baseline (tidak ada entri baru)
10. Tutup modal `Changelog: Custom Asset ID` dengan `✕`
11. Buka Fixed Asset > Assets > All Assets dari sidebar
12. Verifikasi dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]`
13. Klik `[Leave]`
14. Verifikasi Asset ID aset A1 sampai A4 tidak berubah
15. Buka System Log aktor pada Detail User aktor
16. Verifikasi tabel System Log termuat dengan header kolom tampil
17. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak ada entri baru)
18. Buka Fixed Asset > Activity Log
19. Verifikasi tabel Activity Log termuat dengan header kolom tampil
20. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)
21. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
22. Verifikasi Separator menampilkan `/ (Slash)` sehingga konfigurasi tersimpan tetap Separator `/ (Slash)`

### TC-FA-CAID-313: Toggle saat entitas Suspended atau Expired ditolak

23. Catat baseline jumlah entri Object `Custom Asset ID` pada Modal Changelog: Custom Asset ID, System Log aktor, dan Activity Log
24. Geser Master Switch ke OFF
25. Klik `[Disable]` pada dialog `Disable Custom Asset ID`
26. Verifikasi toast error `Changes can't be saved while this workspace is suspended or expired.` tampil
27. Verifikasi Master Switch kembali ke posisi ON
28. Tutup toast error (dismiss)
29. Klik tombol `[Changelog]`
30. Verifikasi modal `Changelog: Custom Asset ID` terbuka dan menampilkan tabel riwayat
31. Verifikasi jumlah entri Changelog sama dengan baseline (tidak ada entri baru)
32. Tutup modal `Changelog: Custom Asset ID` dengan `✕`
33. Buka Fixed Asset > Assets > All Assets dari sidebar
34. Verifikasi Asset ID aset A1 sampai A4 tidak berubah
35. Buka System Log aktor pada Detail User aktor
36. Verifikasi tabel System Log termuat dengan header kolom tampil
37. Verifikasi jumlah entri System Log aktor sama dengan baseline (tidak ada entri baru)
38. Buka Fixed Asset > Activity Log
39. Verifikasi tabel Activity Log termuat dengan header kolom tampil
40. Verifikasi jumlah entri Activity Log sama dengan baseline (tidak ada entri baru)

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. TC-FA-CAID-312 dan 313 menyebut anggota entitas Client Suspended dan Client Expired; keduanya diuji lewat perulangan "Untuk setiap ... (langkah 1 sampai 40)" dengan parameter di tabel Role yang diuji (bagian 8b butir 7).
- Spec ini 40 langkah nominal, 80 langkah dengan ekspansi dua entitas, di atas smell 35 langkah. Alasan: satu kelas harness (kelas g dengan pemicu state tenant, `P-5` butir (a)), dua TC memakai halaman dan akun entitas yang sama, dan tiap iterasi berdiri sendiri pada entitas dan akunnya sendiri sehingga kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; langkah yang diulang memakai idiom perulangan, bukan salinan. Blok baca-log berpola (langkah 7 sampai 9, 15 sampai 20, 29 sampai 31, dan 35 sampai 40) tidak dihitung menurut bagian 3 prinsip 13, sehingga langkah di luar blok itu 22 (44 dengan ekspansi).
- `P-5` butir (a) dan S-05: Save dan Toggle yang ditolak server karena entitas Suspended atau Expired adalah pemicu kelas h; asersi "tidak ada entri log baru" memakai baseline sendiri tiap TC (langkah 2 dan 23, S-12). Asersi lain Expected TC-FA-CAID-312 dan 313 (toast error, Master Switch kembali ON, Asset ID A1 sampai A4, dan konfigurasi tersimpan) tetap di spec ini sebagai bagian TC yang sama.
- Anchor positif asersi absence (bagian 8b butir 2): toast error penolakan pada langkah 5 dan 26, modal Changelog terbuka dengan tabel riwayat (langkah 8 dan 30), dan tabel System Log serta Activity Log termuat dengan header kolom (langkah 16, 19, 36, dan 39).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 (ganti akun dan membuka halaman), langkah 2 dan 23 (baseline jumlah entri, S-12), langkah 3, 4, 24, 25 (aksi TC), langkah 6 dan 28 (tutup toast error, dismiss), langkah 7, 10, 29, 32 (membuka dan menutup modal Changelog), langkah 11, 15, 18, 21, 33, 35, 38 (membuka halaman), dan langkah 13 (klik `[Leave]` setelah `Verifikasi` dialog `Unsaved Changes` pada langkah 12, S-08).
- Dismiss toast error (R-12): toast error penolakan identik muncul pada TC-FA-CAID-312 (langkah 5) dan TC-FA-CAID-313 (langkah 26) dan bertahan sampai ditutup. Langkah 6 menutup toast langkah 5 dan langkah 28 menutup toast langkah 26; dismiss pada langkah 6 mencegah toast langkah 5 meloloskan asersi langkah 26 tanpa penolakan Toggle TC-FA-CAID-313, dan langkah 28 mencegah toast bocor ke iterasi entitas berikutnya.
- Konfigurasi tersimpan pada TC-FA-CAID-312 diamati lewat form sesudah meninggalkan halaman (langkah 21 dan 22) karena Separator tersimpan hanya terlihat pada form yang dimuat ulang.
- Pembagian TC lintas spec: TC-FA-CAID-303 sampai 305 ada di spec 098; TC-FA-CAID-306 sampai 309, 337, dan 338 ada di spec 099.
- Temuan untuk QA:
  - Email dan env var password akun Total Control Client Suspended dan Client Expired tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}`); env var adalah usulan.
  - TC-FA-CAID-313 hanya memberi langkah "Buka All Assets", sedangkan Expected b menyebut "tidak ada entri log baru"; TC tidak menyebut surface log yang dibuka. Spec memakai ketiga surface log yang sama dengan TC-FA-CAID-312.
  - TC-FA-CAID-312 Langkah 3 menulis All Assets dan `[Leave]` lebih dulu, lalu Modal Changelog, tanpa menyebut kembali ke tab Custom Asset ID; Modal Changelog hanya tersedia di tab itu. Spec membuka Modal Changelog sebelum meninggalkan form (langkah 7 sampai 10) dan membuka tab Custom Asset ID lagi pada langkah 21; dialog `Unsaved Changes` diasersi lengkap (body dan tombol) pada langkah 12 dan ditangani sesuai S-08 (langkah 12 dan 13).
  - Lokasi System Log aktor tidak tertulis di langkah TC (catatan NC-05 menyebut Detail User aktor); spec mengikuti catatan itu.
  - Post Condition TC-FA-CAID-312 dan 313 kosong; tidak ada yang diasersi.
