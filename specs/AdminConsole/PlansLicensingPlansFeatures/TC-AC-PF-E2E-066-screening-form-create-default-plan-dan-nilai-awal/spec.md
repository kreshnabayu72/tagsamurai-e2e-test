---
id: TC-AC-PF-E2E-066-screening-form-create-default-plan-dan-nilai-awal
title: "Screening Form Create Default Plan dan Nilai Awal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-166
  - TC-AC-PF-167
  - TC-AC-PF-168
coverage:
  web: automated
---

# Screening Form Create Default Plan dan Nilai Awal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`; Global Role Manage plans & licensing Create, Read, Update, Delete), password dari `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman Plans & Licensing > Plans & Features (Default > Active) dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (nilai awal akun aktor); spec ini tidak mengubahnya.
- Data Pre-setup: Dataset Plan A (Default aktif FAMS: Starter Free, Growth, Professional, Enterprise Paid sehingga FAMS penuh dengan 1 Free dan 3 Paid; SIEM: `SIEM` Paid; SAMS tanpa plan). Dataset hanya dibaca; spec ini tidak membuat atau mengubah plan.
- Data Dinamis: tidak ada.
- Kemampuan teknis: fixture BE untuk menyemai dan memulihkan Dataset Pre-setup (idempoten, disediakan tim FE/BE). Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data dirujuk sebagai `Fixture.plansFeatures.<kunci>` dan ditandai di sini sebagai fixture yang belum ada.
- Pengecualian S-06/S-12 butir A-14: Dataset Pre-setup berslot terbatas (1 Free dan 3 Paid per Product) dan nama literal yang menentukan asersi dipakai tanpa suffix; pemulihan Dataset ke keadaan awal oleh fixture BE dijalankan di hook `before` dan `after` serta sebagai langkah penghubung yang tertulis pada Test Steps; data yang dibuat spec ini bersuffix `{runId}-066`.
- State global: Dataset Pre-setup bersama dipulihkan sebagaimana di atas dan suite berjalan serial (`parallel: false`, lihat `suite.md`). Tiap plan yang dibuat spec ini menambah entri Changelog permanen dan mengubah Last Updated tabel List; entri tidak dapat dihapus lewat UI dan tidak diasersi spec ini.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): fixture BE menghapus plan yang dibuat spec dan memulihkan Dataset.

## Test Steps

### TC-AC-PF-166: Screening form Create Default Plan dari tombol + Default Plan

1. Klik `+ Default Plan`
2. Susuri halaman dari atas ke bawah tanpa mengisi apa pun
3. Verifikasi Header: Breadcrumb `Plans & Licensing > Plans & Features > New Default Plan`
4. Verifikasi Body SectionCard Plan: Product dengan placeholder `Select product`
5. Verifikasi Body SectionCard Plan: Plan Name dengan placeholder `Enter plan name`
6. Verifikasi Body SectionCard Plan: Pricing Type berupa radio `Free` / `Paid` tanpa pilihan terpilih
7. Verifikasi Body SectionCard Plan: tidak ada field Template
8. Verifikasi Body SectionCard Capacity Toggles: Capacity pada opsi terkecil
9. Verifikasi Body SectionCard Binary Toggles: seluruh Binary OFF
10. Verifikasi Body SectionCard Feature Suites: seluruh Feature Suites `None`
11. Verifikasi Body: API call quota `—`
12. Verifikasi Body: tidak ada field Brand cap, Supplier cap, TAG Features, Concurrent User, dan Storage
13. Verifikasi Body: field Asset cap belum tampil sebelum Pricing Type Free dipilih pada Product FAMS
14. Verifikasi Footer: Estimated Total, `[Clear Field]`, dan `[Submit]` tampil
15. Verifikasi Footer: tidak ada checkbox Stay on this form

### TC-AC-PF-167: Nilai awal form Create Default Plan: Capacity opsi terkecil, Binary OFF, Feature Suites None

16. Pilih Product `SAMS`
17. Amati nilai semua field di SectionCard Capacity Toggles, Binary Toggles, dan Feature Suites
18. Verifikasi Capacity: Asset Name cap `10`
19. Verifikasi Capacity: Group count `1`
20. Verifikasi Capacity: Group hierarchy depth `1`
21. Verifikasi Capacity: Category count `5`
22. Verifikasi Capacity: Category hierarchy depth `1`
23. Verifikasi Capacity: Scheduled reports `—`
24. Verifikasi Capacity: API call quota `—`
25. Verifikasi Binary Toggles semua OFF
26. Verifikasi Feature Suites semua `None`
27. Klik `[Clear Field]`

### TC-AC-PF-168: Dropdown Product Create Default Plan menyembunyikan Product yang slot Free dan Paid-nya sudah penuh

28. Klik dropdown Product
29. Verifikasi opsi `SAMS` dan `SIEM` tampil
30. Verifikasi opsi `FAMS` tidak ada (penuh per Invariant #1 dan #2)

## Notes

- Langkah penghubung (S-03): `[Clear Field]` sebelum blok TC-AC-PF-168 mengembalikan form ke keadaan bersih (Product `Select product`) supaya dropdown diamati dari keadaan awal dan form tidak berakhir dirty (S-09). Setelah blok TC-AC-PF-168 form tetap bersih karena tidak ada opsi yang dipilih.
- Urutan asersi pada TC-AC-PF-168 menempatkan opsi yang tampil (`SAMS`, `SIEM`) sebelum asersi absence opsi `FAMS` sebagai anchor positif pada dropdown yang sama (bagian 8b butir 2).
- Pengecualian S-06/S-12 butir A-14 tidak memakai target aksi tulis pada spec ini; nama literal Dataset Plan A (`SIEM`, `Growth`, `Starter`) hanya dibaca.
- Temuan untuk QA:
-   - Post Condition TC yang tidak punya langkah observasi di TC (mis. `Tidak ada perubahan data`, `Default plan ... tersimpan`) tidak diasersi.
-   - TC-AC-PF-166 Expected b.ii menyebut Capacity ke opsi terkecil tanpa menyebut nilai angkanya; asersi spec mengikuti teks TC, sedangkan nilai tiap field Capacity baru ditulis pada TC-AC-PF-167 (SAMS).
