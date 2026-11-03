---
id: TC-FA-CF-E2E-073-edit-konflik-opsi-dihapus-dan-asset-name-dihapus-aktor-lain
title: "Edit: Opsi Dropdown Dihapus atau Diganti Aktor Lain Saat Modal Terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-260
  - TC-FA-CF-261
coverage:
  web: automated
---

# Edit: Opsi Dropdown Dihapus atau Diganti Aktor Lain Saat Modal Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor UI sesi 1: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Akun pelaku sesi 2 (Pre-setup #28): Total Control sesi 2 Company Nilai (pengguna Rina Putri, Pre-setup #10). Email akun ini tidak tertulis di Pre-setup TC; disediakan tim FE. Dipakai dua cara: sesi API (login API dengan `Spectra.env.FA_TC2_NILAI_PASSWORD`, token tidak dihitung sebagai sesi web) untuk memicu perubahan opsi, dan login UI sesudah semua aksi untuk membaca System Log `Rina Putri` (ganti akun eksplisit pada langkah bersangkutan).
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`; aset A1 = `Gold`; berada di halaman pertama tabel). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Kemampuan teknis: membaca jumlah dan isi entri Changelog tab General, Activity Log, dan System Log per aktor (disediakan tim FE/BE); sesi API untuk mengubah opsi Dropdown.
- Waktu: jam server dan jam browser sinkron; Date entri log dibandingkan dengan waktu yang dicatat sesudah penghapusan oleh sesi API dengan toleransi satu menit (S-12).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan `Brand Tier` ke baseline, mengembalikan sesi UI ke akun default suite (Total Control Company Alpha), dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite untuk akun sesi 1 dan sesi 2; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-261: Rename opsi oleh admin lain bukan stale dan Save sukses

1. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
2. Ubah toggle Required ke Yes
3. Sesi API (Rina Putri) mengganti nama opsi `Gold` menjadi `Gold Plus` pada `Brand Tier` hingga perubahan tersimpan
4. Klik `[Save]`
5. Verifikasi toast sukses `Success, custom field has been updated.` tampil
6. Verifikasi pesan inline `Gold no longer exists. Please select another.` tidak tampil

### TC-FA-CF-260: Save yang merujuk opsi yang sudah dihapus admin lain ditolak dengan pesan stale inline

7. Catat jumlah entri Changelog tab General, Activity Log, dan System Log `Sarah Johnson`
8. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
9. Ubah nama opsi `Silver` menjadi `Platinum` pada form
10. Sesi API (Rina Putri) menghapus opsi `Silver` pada `Brand Tier` hingga perubahan tersimpan
11. Catat waktu sesudah sesi API menyimpan
12. Klik `[Save]`
13. Verifikasi pesan inline `Silver no longer exists. Please select another.` tampil pada Dropdown Options
14. Verifikasi modal tetap terbuka
15. Verifikasi seluruh input dipertahankan
16. Klik icon close `[✕]`
17. Verifikasi dialog `Unsaved Changes` tampil
18. Klik `[Leave]`
19. Verifikasi kolom Value Setting baris `Brand Tier` tidak memuat `Platinum` dan tidak memuat `Silver` (tidak ada mutasi dari Save sesi 1)
20. Buka Modal Changelog tab General, Activity Log, dan System Log `Sarah Johnson` lalu hitung ulang jumlah entri masing-masing, kemudian kembali ke tab General
21. Verifikasi Changelog bertambah tepat satu entri Edit properti `Dropdown Options` untuk `Brand Tier` dibanding baseline (penghapusan `Silver` oleh sesi 2)
22. Verifikasi Activity Log bertambah tepat satu entri Edit properti `Dropdown Options` untuk `Brand Tier` dibanding baseline (penghapusan `Silver` oleh sesi 2)
23. Verifikasi jumlah entri System Log `Sarah Johnson` sama dengan baseline langkah 7 (tidak ada entri baru dari Save sesi 1)
24. Ganti akun: `Logout` dari Total Control Company Nilai (Sarah Johnson)
25. Login sebagai Total Control sesi 2 Company Nilai (Rina Putri) dengan `Spectra.env.FA_TC2_NILAI_PASSWORD`
26. Buka System Log `Rina Putri`
27. Verifikasi System Log `Rina Putri` memuat entri Edit properti `Dropdown Options` untuk `Brand Tier` yang menghapus `Silver` dengan Date sesuai waktu yang dicatat (toleransi satu menit)
28. `Logout` dari Total Control sesi 2 Company Nilai (Rina Putri)

## Notes

- Urutan TC di spec: 261, 260. Kasus Save sukses (261) berjalan lebih dulu; kasus 260 mengakhiri spec dengan pembacaan log dan ganti akun. Keadaan `Brand Tier` setelah TC-FA-CF-261 (opsi `Gold Plus`, `Silver`, `Bronze`; Required Yes) tidak mengubah prakondisi TC-FA-CF-260 karena yang diuji adalah opsi `Silver`.
- Pelaku sesi 2 memicu perubahan state lewat sesi API (bukan konteks kedua kelas c); hasilnya diasersi di sesi UI pertama dan di sesi UI kedua (log). Langkah 3 dan 10 ditulis "... hingga ... tersimpan" (R-20).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (baseline jumlah entri dicatat sesudah TC-FA-CF-261, karena Save TC itu sendiri menambah entri), langkah 11 (mencatat waktu untuk asersi Date), langkah 16 sampai 18 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 20 (membuka tiga surface log), langkah 24 sampai 26 dan 28 (ganti akun eksplisit ke sesi 2 untuk membaca System Log `Rina Putri`, lalu logout; hook `after` mengembalikan sesi ke akun default suite).
- Spec ini bukan konteks UI ganda yang berjalan bersamaan: sesi 2 dipakai berurutan setelah semua aksi UI sesi 1, sehingga satu akun web aktif pada satu waktu.
- Langkah 21 dan 22 mengasersi selisih tepat satu entri terhadap baseline (S-12) sehingga entri dari Save sesi 1 yang tidak boleh ada terdeteksi. Langkah 23 mengasersi jumlah entri System Log `Sarah Johnson` sama dengan baseline langkah 7 (TC-FA-CF-260 butir c: tidak bertambah entri baru dibanding sebelum langkah 4), bukan absence entri `Brand Tier`, karena audit trail permanen sudah memuat entri `Brand Tier` dari langkah 5 dan dari spec lain.
- Temuan untuk QA:
  - TC-FA-CF-260 dan TC-FA-CF-261 tidak menyebut mekanisme "sesi 2" atau "sesi lain"; spec memakai sesi API untuk pelaku yang hanya memicu perubahan opsi.
  - Penghapusan `Silver` (TC-FA-CF-260) dan penggantian nama `Gold` (TC-FA-CF-261) sama-sama menghasilkan entri Edit properti `Dropdown Options` untuk `Brand Tier` di System Log `Rina Putri`; spec membedakannya lewat Date dan isi entri (menghapus `Silver`), yang tidak dirinci di TC.
  - Cara membuka System Log aktor, System Log `Rina Putri`, dan Activity Log tidak dijelaskan di TC (menu atau jalur navigasi); spec menulisnya persis seperti TC.
  - Email Total Control Company Nilai (sesi 1 dan sesi 2) serta env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` dan `FA_TC2_NILAI_PASSWORD` yang disediakan tim FE.
