---
id: TC-FA-CF-E2E-079-menutup-form-edit-unsaved-changes-dan-backdrop
title: "Menutup Form Edit: Unsaved Changes dan Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-291
  - TC-FA-CF-292
  - TC-FA-CF-293
  - TC-FA-CF-294
coverage:
  web: automated
---

# Menutup Form Edit: Unsaved Changes dan Backdrop

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Nilai (pengguna Sarah Johnson, Modified By `Sarah J`; Pre-setup #1 dan #18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); pola `totalControl_automated_{namaCompany}@qwertysystem.net`, disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_NILAI_PASSWORD`; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Company Nilai (#18, dasar Company Alpha #11 dan baseline #12; 21 field tab General): dipakai `Legacy Tag` (Text, Scope kosong). Spec tidak menyimpan perubahan; nilai yang diketik pada Field Name hanya untuk membuat form dirty. Nilai data mengacu `Fixture.faCustomFields.nilai` (fixture baru, disediakan tim FE).
- Baseline: hook `before` memulihkan baseline Company Nilai lewat seed reset Company; hook `after` membersihkan data Dinamis milik spec. Mekanisme seed disediakan tim FE/BE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel oleh hook `before` dan `after` suite; lihat `suite.md`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Atur ukuran halaman Pagination menjadi 100

### TC-FA-CF-291: Menutup modal Edit tanpa perubahan tidak menampilkan dialog Unsaved Changes

2. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`
3. Klik icon close `[✕]`
4. Verifikasi modal langsung tertutup
5. Verifikasi dialog `Unsaved Changes` tidak tampil

### TC-FA-CF-292: Menutup modal Edit yang diubah menampilkan dialog Unsaved Changes

6. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`
7. Ubah Field Name menjadi `Dirty Edit`
8. Klik icon close `[✕]`
9. Verifikasi dialog `Unsaved Changes` dengan `You have unsaved changes. Are you sure you want to leave?`, `[Cancel]`, dan `[Leave]` tampil
10. Klik `[Leave]`
11. Verifikasi modal tertutup
12. Verifikasi baris `Legacy Tag` tetap bernama `Legacy Tag` pada tabel (tidak disimpan)

### TC-FA-CF-293: Mengubah lalu mengembalikan nilai ke nilai tersimpan dianggap clean

13. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`
14. Ubah Field Name menjadi `Legacy Tag X`
15. Ubah Field Name kembali menjadi `Legacy Tag`
16. Klik icon close `[✕]`
17. Verifikasi modal langsung tertutup
18. Verifikasi dialog `Unsaved Changes` tidak tampil

### TC-FA-CF-294: Klik backdrop modal Edit tidak menutup modal

19. Klik row action `⋯` > `Edit` pada baris `Legacy Tag`
20. Ubah Field Name menjadi `Dirty Bd`
21. Klik area backdrop di luar modal
22. Verifikasi modal tetap terbuka
23. Verifikasi input dipertahankan: Field Name masih `Dirty Bd`
24. Verifikasi tidak ada dialog `Unsaved Changes`
25. Klik icon close `[✕]`
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`

## Notes

- Urutan TC di spec: 291, 292, 293, 294. Jumlah pembukaan modal sama dengan jumlah penutupan (bagian 3 prinsip 6); spec tidak menyimpan perubahan apa pun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (ukuran halaman 100 supaya seluruh baris Company Nilai tampil dan baris target ditemukan tanpa Search), langkah 25 sampai 27 (menutup form dirty pada akhir TC-FA-CF-294 supaya spec tidak berakhir dengan form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- Nilai yang diketik (`Dirty Edit`, `Legacy Tag X`, `Dirty Bd`) tidak disimpan sehingga tidak bersuffix.
- Temuan untuk QA:
  - Expected a TC-FA-CF-292 mencantumkan teks dialog `Unsaved Changes` dan Expected b "menutup modal tanpa menyimpan"; spec mengasersi tidak tersimpan lewat nama baris di tabel karena TC tidak memberi langkah observasi lain.
  - Email Total Control Company Nilai dan env var passwordnya tidak tertulis di Pre-setup TC; spec memakai `FA_TC_NILAI_PASSWORD` yang disediakan tim FE.
