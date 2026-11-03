---
id: TC-FA-CF-E2E-020-screening-modal-create-default-dan-aksesibilitas
title: "Screening Modal Create: Nilai Default, Label Radio, dan Aksesibilitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-52
  - TC-FA-CF-53
  - TC-FA-CF-201
  - TC-FA-CF-200
coverage:
  web: automated
---

# Screening Modal Create: Nilai Default, Label Radio, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup (S-06).
- Data Pre-setup: tidak ada data yang dibuat atau diubah; spec hanya membuka, mengamati, dan menutup modal Create.
- Kemampuan teknis: pembacaan atribut DOM (`aria-required`, `role`, `aria-modal`) pada modal dan dialog; navigasi keyboard Tab antar kontrol modal.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): spec ini tidak menyimpan data; hook `after` suite tetap memulihkan baseline Company.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

#### TC-FA-CF-52: Screening modal Create Custom Field

1. Klik `[+ Custom Field]`
2. Verifikasi Header modal menampilkan judul `Create Custom Field`
3. Verifikasi Header modal menampilkan icon close `[✕]`
4. Verifikasi `Field Name *` berupa input teks dengan placeholder `Enter field name`
5. Verifikasi `Data Type *` berupa dropdown dengan placeholder `Select data type`
6. Verifikasi `Data Type *` tampil tanpa helper
7. Verifikasi icon ℹ tampil di samping label `Data Type *`
8. Verifikasi `Placeholder` berupa input teks opsional
9. Verifikasi `Scope *` menampilkan radio `General (Applies to all assets)` terpilih dan radio `Specific Asset Name`
10. Verifikasi `Value Type *` menampilkan radio `Specific (Each asset has its own unique value)` terpilih dan radio `Global`
11. Verifikasi toggle `Required` pada posisi No
12. Verifikasi kontrol Values, Decimal Places, dan Formula Builder belum tampil
13. Verifikasi urutan Body dari atas ke bawah: `Field Name *`, `Data Type *`, `Placeholder`, `Scope *`, `Value Type *`, toggle `Required`
14. Verifikasi checkbox `Stay on this form after submitting` tampil tidak dicentang
15. Verifikasi checkbox `Stay on this form after submitting` berada tepat di atas baris tombol
16. Verifikasi tombol `[Clear Field]` dan `[Submit]` tampil rata kanan

#### TC-FA-CF-53: Nilai default form Create sesuai Defaults dan Ordering Spec

17. Verifikasi Scope default `General`
18. Verifikasi Value Type default `Specific`
19. Verifikasi Required default No
20. Verifikasi tidak ada kontrol switch Active di modal

#### TC-FA-CF-201: Label radio Value Type Global tidak memuat catatan spesifikasi

21. Verifikasi radio Value Type berlabel `Specific (Each asset has its own unique value)` dan `Global (One shared value)`

#### TC-FA-CF-200: Modal Create memenuhi atribut aksesibilitas yang dinyatakan PRD

22. Verifikasi input `Field Name` dan `Data Type` memiliki `aria-required="true"`
23. Pilih Data Type `Text`
24. Pilih Value Type `Global`
25. Verifikasi input Global Value memiliki `aria-required="true"`
26. Pilih Scope `Specific Asset Name`
27. Verifikasi input Asset Name memiliki `aria-required="true"`
28. Pilih Data Type `Dropdown`
29. Verifikasi input Values memiliki `aria-required="true"`
30. Tekan Tab berulang dari kontrol pertama modal sampai kontrol terakhir
31. Verifikasi Tab berpindah berurutan melintasi seluruh kontrol modal
32. Klik `[✕]` (memicu dialog konfirmasi)
33. Verifikasi dialog `Unsaved Changes` tampil
34. Verifikasi dialog memiliki `role="dialog"`
35. Verifikasi dialog memiliki `aria-modal="true"`
36. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `####` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 52, 53, 201, 200 (urutan sumber 52, 53, 200, 201). TC-FA-CF-201 diletakkan sebelum TC-FA-CF-200 karena kontrol Value Type tersembunyi setelah Data Type `Dropdown` dipilih pada TC-FA-CF-200, dan TC-FA-CF-200 mengubah form sehingga ditutup lewat dialog di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`): memilih Data Type `Text`, Value Type `Global`, Scope `Specific Asset Name`, dan Data Type `Dropdown` pada TC-FA-CF-200 agar tiap input wajib tampil; langkah 32 memicu dialog konfirmasi yang diamati atributnya (TC tidak memberi langkah pemicunya, lihat Temuan untuk QA) dan penutupan form dirty mengikuti S-08.
- Spec ini 36 langkah, di atas smell 35 langkah (bagian 3 prinsip 13): satu modal Create dibuka sekali untuk empat TC screening satu topik; Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan tidak ada langkah yang dapat dihapus tanpa melepas klausa Expected.
- Expected TC-FA-CF-200 butir a menyebut Placeholder, toggle Required, dan checkbox Stay tidak diassert; spec mengikuti dan tidak menulis asersi untuk ketiganya.
- Temuan untuk QA:
  - TC-FA-CF-52 menulis label radio Value Type kedua sebagai `Global`, sedangkan TC-FA-CF-201 (keputusan NC-22) menulis `Global (One shared value)`. Spec mengikuti masing-masing TC apa adanya; salah satu asersi akan gagal bila label sebenarnya `Global (One shared value)`. Mohon TC-FA-CF-52 diseragamkan.
  - TC-FA-CF-200 butir b ('Dialog konfirmasi yang muncul') tidak memuat langkah pemicu dialog. Spec memakai `Klik [✕]` pada form dirty yang memunculkan dialog `Unsaved Changes`.
  - TC-FA-CF-200 butir c tidak menyebut urutan Tab yang benar; spec mengasersi 'berurutan melintasi seluruh kontrol modal' tanpa menetapkan urutan konkret.
  - TC-FA-CF-52 butir Body 'berurutan' ditulis sebagai satu `Verifikasi` urutan tambahan di samping `Verifikasi` tiap kontrol.
