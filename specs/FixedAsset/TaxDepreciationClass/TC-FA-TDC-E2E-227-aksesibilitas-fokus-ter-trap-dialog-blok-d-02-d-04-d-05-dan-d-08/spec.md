---
id: TC-FA-TDC-E2E-227-aksesibilitas-fokus-ter-trap-dialog-blok-d-02-d-04-d-05-dan-d-08
title: "Aksesibilitas Fokus Ter-trap Dialog Blok D-02, D-04, D-05 dan D-08"
layer: ui-e2e
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-918
  - TC-FA-TDC-920
sourceRules: ["§4.5#b2", "§4.5#b1", "§4.1.1#r16", "D-04", "D-05", "§4.2c#b1", "D-08"]
smoke: []
dependsOn: []
trace:
  "§4.5#b2": [3, 10, 17, 25]
  "§4.5#b1": [5, 12, 19, 27]
  "§4.1.1#r16": 6
  "D-04": 13
  "D-05": 20
  "§4.2c#b1": 29
  "D-08": 31
coverage:
  web: automated
---

# Aksesibilitas Fokus Ter-trap Dialog Blok D-02, D-04, D-05 dan D-08

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. NB-1 (Used By 5) memicu dialog blok D-02 dan D-04; NB-2 (Used By 3) memicu dialog blok D-05. Tidak ada data berubah.
- Data Dinamis (milik spec, dibuat di hook `before` lewat seeding API, dihapus di `after`; kunci `khsV8`): class Non-building `KHS-V8-{runId}-227` (Class Name ditetapkan tim FE) dengan Useful Life 8, Allowed Methods Straight Line dan Declining Balance, Used By 2 lewat dua Asset Class pemakai `AC-DB1 – Pompa Air Gudang` dan `AC-DB2 – Genset Pabrik` yang keduanya memakai Declining Balance. Bersama sembilan class di atas tabel berisi 10 baris pada satu halaman (page size default 10), sehingga baris dicari tanpa Search.
- Kemampuan teknis: seeding class dan Asset Class pemakai lewat API (`suite.md`); menekan `Tab` berulang dan `Esc`; mengamati posisi fokus di dalam dialog; menutup Drawer dirty lewat `[×]` dan `[Leave]` (S-08).
- State global yang diubah: tidak ada (semua dialog dibatalkan; Drawer D-08 ditutup tanpa menyimpan).

## Test Steps

### TC-FA-TDC-918: Fokus ter-trap di dialog blok D-02, D-04, dan D-05 dan Esc menutup

1. Klik toggle `Active` baris NB-1 sehingga dialog D-02 muncul
2. Tekan Tab berulang
3. Verifikasi D-02: fokus tetap di dalam dialog pada satu-satunya tombol `[OK]`
4. Tekan Esc
5. Verifikasi dialog D-02 tertutup
6. Verifikasi toggle `Active` NB-1 tetap On
7. Klik tombol `⋯` baris NB-1
8. Klik `Delete` sehingga dialog D-04 muncul
9. Tekan Tab berulang
10. Verifikasi D-04: fokus tetap pada `[OK]`
11. Tekan Esc
12. Verifikasi dialog D-04 tertutup
13. Verifikasi NB-1 tidak terhapus
14. Klik tombol `⋯` baris NB-2
15. Klik `Delete` sehingga dialog D-05 muncul
16. Tekan Tab berulang
17. Verifikasi D-05: fokus tetap pada `[OK]`
18. Tekan Esc
19. Verifikasi dialog D-05 tertutup
20. Verifikasi NB-2 tidak terhapus

### TC-FA-TDC-920: Fokus ter-trap di dialog blok D-08 dan Esc menutup

21. Klik link Class Code `KHS-V8-{runId}-227` pada tabel
22. Lepas `Declining Balance` dari Allowed Methods
23. Klik `[Save]` sehingga dialog D-08 muncul
24. Tekan Tab berulang
25. Verifikasi D-08: fokus tetap di dalam dialog pada satu-satunya tombol `[OK]` dan tidak keluar ke halaman
26. Tekan Esc
27. Verifikasi dialog D-08 tertutup
28. Klik `[×]` pada header Drawer
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`
31. Verifikasi Allowed Methods baris `KHS-V8-{runId}-227` tetap `Straight Line · Declining Balance` (tidak ada yang tersimpan)

## Notes

- Urutan TC dalam spec: TC-FA-TDC-918 sebelum TC-FA-TDC-920 karena TC-FA-TDC-920 membuka Drawer dirty yang ditutup di akhir spec (prinsip 6 bagian 3).
- Langkah penghubung (S-03): langkah 28 sampai 30 (menutup Drawer dirty secara deterministik; S-08; dialog `Unsaved Changes` sudah dicakup S-08 dan tidak dicatat terpisah) dan langkah 31 (observasi "tidak ada yang tersimpan" lewat kolom Allowed Methods pada tabel setelah Drawer ditutup; TC tidak memberi langkah observasi, lihat Temuan untuk QA).
- Asersi absence "NB-1 tidak terhapus" (langkah 13) dan "NB-2 tidak terhapus" (langkah 20) didahului anchor positif: dialog tertutup pada langkah 12 dan 19 serta baris lain pada tabel yang sama masih tampil sebagai pembanding (8b.2).
- Tiap dialog dibuka dari datanya sendiri; tidak ada aksi yang menghapus atau mengubah data karena semua dialog dibatalkan.
- Temuan untuk QA:
  - TC-FA-TDC-920 Expected b ("tidak ada yang tersimpan") tidak memberi langkah observasi; spec mengamatinya pada kolom Allowed Methods tabel sesudah Drawer ditutup lewat `[Leave]`.
  - TC-FA-TDC-920 hanya menyebut Class Code `KHS-V8` tanpa suffix; spec memakai `KHS-V8-{runId}-227` (S-12); batas panjang Class Code tidak disebut TC.
  - TC-FA-TDC-918 tidak menyebut Used By atau status NB-2 yang memicu D-05; spec memakai NB-2 dengan Used By 3 sesuai Example Data.
  - Email akun Total Control tidak tertulis di TC.
