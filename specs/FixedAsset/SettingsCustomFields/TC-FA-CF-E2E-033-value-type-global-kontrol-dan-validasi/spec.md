---
id: TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi
title: "Value Type Global: Kontrol dan Validasi Nilai Kosong"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-99
  - TC-FA-CF-100
  - TC-FA-CF-101
  - TC-FA-CF-102
  - TC-FA-CF-103
  - TC-FA-CF-104
coverage:
  web: automated
---

# Value Type Global: Kontrol dan Validasi Nilai Kosong

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup (hanya dibaca): Asset Name `Generator` dan `Pump` Company Alpha (Pre-setup #11).
- Data dinamis: tidak ada field yang disimpan; nilai yang hanya diketik: Field Name `Global Empty {runId}-033`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-99: Value Type Global dengan Scope General menampilkan satu input Value

1. Klik `[+ Custom Field]`
2. Pilih Data Type `Text`
3. Pilih Value Type `Global`
4. Verifikasi satu input berlabel `Value` tampil dengan placeholder `Enter global value`
5. Verifikasi input `Value` menampilkan helper `Shown as read-only on asset details`

#### TC-FA-CF-100: Value Type Global dengan Scope Specific menampilkan satu input per Asset Name berlabel nama Asset Name

6. Klik `[Clear Field]`
7. Pilih Data Type `Text`
8. Pilih Scope `Specific Asset Name` dengan `Generator` dan `Pump`
9. Pilih Value Type `Global`
10. Verifikasi dua input berlabel `Generator` dan `Pump` tampil
11. Hapus chip `Pump`
12. Verifikasi hanya input berlabel `Generator` yang tersisa

#### TC-FA-CF-101: Kontrol Value Type disembunyikan untuk Data Type Dropdown

13. Klik `[Clear Field]`
14. Pilih Data Type `Text`
15. Pilih Value Type `Global`
16. Ganti Data Type menjadi `Dropdown`
17. Verifikasi kontrol Value Type tidak tampil

#### TC-FA-CF-102: Kontrol Value Type disembunyikan untuk Data Type Multi-Dropdown

18. Klik `[Clear Field]`
19. Pilih Data Type `Text`
20. Pilih Value Type `Global`
21. Ganti Data Type menjadi `Multi-Dropdown`
22. Verifikasi kontrol Value Type tidak tampil

#### TC-FA-CF-103: Kontrol Value Type disembunyikan untuk Data Type Formula

23. Klik `[Clear Field]`
24. Pilih Data Type `Text`
25. Pilih Value Type `Global`
26. Ganti Data Type menjadi `Formula`
27. Verifikasi kontrol Value Type tidak tampil

#### TC-FA-CF-104: Value Type Global dengan input Value kosong ditolak saat Submit

28. Klik `[Clear Field]`
29. Isi Field Name `Global Empty {runId}-033`, Data Type `Text`, Value Type `Global`, input Value dikosongkan
30. Klik `[Submit]`
31. Verifikasi pesan inline `Value must not be empty` tampil di bawah input Value
32. Verifikasi modal tetap terbuka
33. Klik `[✕]`
34. Verifikasi dialog `Unsaved Changes` tampil
35. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`): `Klik [Clear Field]` di antara kasus yang hanya mengubah kontrol tanpa menyimpan (halaman yang sama dipakai berulang) dan penutupan form dirty pada langkah 33 dan dua langkah berikutnya (S-08).
- Field Dinamis bernama bersuffix `{runId}-033` (S-12); `{runId}` hanya terdiri atas digit. Data Pre-setup hanya dibaca.
- Temuan untuk QA:
  - TC-FA-CF-101, 102, dan 103 butir b ('Value Type tersimpan nanti sebagai Specific') tidak punya langkah observasi dan TC bertipe UI Only (tanpa Submit); spec tidak mengasersinya dan tidak menambah langkah Submit (S-01, S-15). Usulan: tambahkan langkah Submit dan pembacaan kolom Value Type pada TC itu.
  - TC-FA-CF-99 butir 'Satu input berlabel `Value`' menyatukan label, placeholder, dan helper; spec memecah helper menjadi `Verifikasi` tersendiri (S-01).
