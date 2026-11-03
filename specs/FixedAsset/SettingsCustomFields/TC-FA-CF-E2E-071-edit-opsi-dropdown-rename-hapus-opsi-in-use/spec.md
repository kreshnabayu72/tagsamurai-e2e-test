---
id: TC-FA-CF-E2E-071-edit-opsi-dropdown-rename-hapus-opsi-in-use
title: "Edit Opsi Dropdown: Rename dan Hapus Opsi yang Dipakai Aset"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-248
  - TC-FA-CF-249
  - TC-FA-CF-251
  - TC-FA-CF-252
  - TC-FA-CF-253
coverage:
  web: automated
---

# Edit Opsi Dropdown: Rename dan Hapus Opsi yang Dipakai Aset

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Brand Tier` (Dropdown `Gold`, `Silver`, `Bronze`; aset A1 = `Gold`) dan `Accessories` (Multi-Dropdown `Charger`, `Cable`, `Case`; A1 = `Charger` dan `Cable`, A2 = `Cable`). Kedua field berada di halaman pertama tabel (urutan Field Name A-Z). Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` memulihkan field baseline yang diubah spec (`Brand Tier`, `Accessories`, beserta nilai A1 dan A2) dan membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE, termasuk pemulihan field `Brand Tier` di tengah spec (lihat Notes).
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah selain data Company Nilai yang dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-249: Menghapus opsi yang sedang dipakai aset menampilkan dialog Remove Value

1. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
2. Klik `✕` pada badge `Gold`
3. Verifikasi dialog konfirmasi `Remove Value` dengan teks `This value is currently used in assets. Removing it will clear this value from those assets. This action cannot be undone.` serta tombol `[Cancel]` dan `[Remove]` tampil

### TC-FA-CF-251: Remove pada dialog menghapus opsi dan baru berlaku saat Save

4. Klik `[Remove]`
5. Verifikasi badge `Gold` hilang dari form
6. Verifikasi belum ada perubahan data sebelum `[Save]`: modal tetap terbuka dan toast `Success, custom field has been updated.` belum tampil
7. Klik `[Save]`
8. Verifikasi toast sukses `Success, custom field has been updated.` tampil
9. Buka Detail aset `A1`
10. Verifikasi nilai aset `A1` untuk field `Brand Tier` dikosongkan
11. Kembali ke Fixed Asset > Settings > Custom Fields (tab General)
12. Pulihkan field `Brand Tier` ke baseline (opsi `Gold`, `Silver`, `Bronze`; aset `A1` = `Gold`) lewat seed API
13. Muat ulang halaman (F5)

### TC-FA-CF-248: Rename opsi yang sedang dipakai aset tersimpan tanpa dialog

14. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
15. Klik badge `Gold` dan ubah menjadi `Platinum`
16. Klik `[Save]`
17. Verifikasi dialog konfirmasi tidak tampil
18. Verifikasi toast sukses `Success, custom field has been updated.` tampil
19. Verifikasi kolom Value Setting baris `Brand Tier` menampilkan `Platinum, Silver` dengan `+1 more` sesuai urutan dan posisi opsi dipertahankan

### TC-FA-CF-252: Menghapus opsi yang belum dipakai aset tidak menampilkan dialog

20. Klik row action `⋯` > `Edit` pada baris `Brand Tier`
21. Klik `✕` pada badge `Bronze`
22. Tunggu toast lama hilang otomatis
23. Klik `[Save]`
24. Verifikasi dialog `Remove Value` tidak tampil
25. Verifikasi toast sukses `Success, custom field has been updated.` tampil
26. Verifikasi opsi `Bronze` hilang dari field: kolom Value Setting baris `Brand Tier` menampilkan `Platinum, Silver` tanpa chip `+1 more`

### TC-FA-CF-253: Menghapus opsi in-use pada Multi-Dropdown hanya mengeluarkan opsi itu dari nilai tiap aset

27. Klik row action `⋯` > `Edit` pada baris `Accessories`
28. Klik `✕` pada badge `Charger`
29. Klik `[Remove]` pada dialog `Remove Value`
30. Tunggu toast lama hilang otomatis
31. Klik `[Save]`
32. Verifikasi toast sukses `Success, custom field has been updated.` tampil
33. Buka Asset Detail `A1`
34. Verifikasi nilai field `Accessories` pada Asset Detail `A1` tersisa `Cable`
35. Buka Asset Detail `A2`
36. Verifikasi nilai field `Accessories` pada Asset Detail `A2` tetap `Cable`

## Notes

- Urutan TC di spec: 249, 251, 248, 252, 253. TC-FA-CF-249 dan 251 berantai pada modal yang sama (pembukaan dialog `Remove Value`, lalu `[Remove]` dan `[Save]`). TC-FA-CF-251 menghapus opsi `Gold` yang dipakai A1, padahal TC-FA-CF-248 membutuhkan `Gold` yang dipakai A1; karena itu `Brand Tier` dipulihkan lewat seed di antara keduanya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (mengonfirmasi dialog `Remove Value` yang menjadi aksi TC-FA-CF-251), langkah 11 sampai 13 (kembali ke halaman Custom Fields, memulihkan `Brand Tier` lewat seed, dan memuat ulang halaman supaya tabel mencerminkan seed; `Brand Tier` dan `Accessories` berada di halaman pertama sehingga ukuran halaman tidak diubah), langkah 29 (mengonfirmasi dialog `Remove Value` yang menjadi aksi TC-FA-CF-253).
- Langkah 6 mengasersi klausa "belum ada perubahan data sebelum Save" lewat keadaan modal; TC tidak memberi langkah observasi lain untuk klausa itu (lihat Temuan untuk QA).
- Spec melewati sekitar 35 langkah (36 langkah). Seluruhnya satu topik (Edit opsi Dropdown dan Multi-Dropdown), satu akun, satu dataset Company Nilai; kelebihan di atas 35 hanya berasal dari dua langkah penghubung toast (R-22).
- Langkah penghubung toast (S-03, R-22): langkah 22 dan 30 (`Tunggu toast lama hilang otomatis`, aksi tanpa `Verifikasi`) mendahului aksi yang menghasilkan toast sukses berteks sama dengan toast yang sudah diasersi sebelumnya; `Verifikasi` toast berikutnya tidak membaca toast lama.
- Temuan untuk QA:
  - Expected a TC-FA-CF-251 "belum ada perubahan data sebelum `[Save]`" tidak menyebut cara cek; spec mengasersi lewat modal yang masih terbuka dan toast sukses yang belum tampil.
  - Halaman Detail aset `A1` dan `A2` serta cara membukanya tidak dijelaskan di TC; spec menulisnya persis seperti TC.
  - TC-FA-CF-252 menyebut "opsi `Bronze` hilang dari field" tanpa menyebut surface; spec mengasersi lewat kolom Value Setting (dua badge tanpa chip `+1 more`).
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
