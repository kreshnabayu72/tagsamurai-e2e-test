---
id: TC-GS-FILEMGR-E2E-068-storage-isolasi-client
title: "Kartu Storage Usage Hanya Memuat Data Client Aktif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-281
coverage:
  web: automated
---

# Kartu Storage Usage Hanya Memuat Data Client Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Sinta Maharani (`Sinta M`) Client A `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup A1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script.
- Suite serial (`parallel: false`) karena spec mengubah laporan Storage. Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE; mekanisme laporan app dan Client B tidak didefinisikan di TC, lihat Temuan untuk QA): seeding laporan Storage skenario S1 untuk Client A (Tabel A5: kuota 50 GB; Fixed Asset 3.2 GB, Admin Console 1.4 GB, Global Settings 204.8 MB; Total Used 4.8 GB) dan skenario S6 untuk Client B (kuota 200 GB; Fixed Asset 10.0 GB, 14/09/26 02:00). Tidak ada login ke Client B; Client B hanya data pembanding.
- State global yang diubah: laporan Storage Client A dan Client B. Hook `after` (tetap jalan walau spec gagal di tengah) memulihkan laporan Storage awal kedua Client.
- Dependensi TC (TC-268 kartu Storage Usage) dijalankan sebagai langkah aksi di spec ini.
- Cleanup (hook `after`): pulihkan laporan Storage seperti di atas.

## Test Steps

### TC-GS-FILEMGR-281: Kartu hanya memuat laporan dan kuota Client aktif

1. Siapkan laporan Storage skenario S1 untuk Client A dan skenario S6 untuk Client B lewat fixture BE
2. Muat ulang Global Settings > File Manager sebagai user Client A
3. Baca seluruh isi kartu Storage Usage
4. Verifikasi `Total Used` `4.8 GB`
5. Verifikasi `Storage Quota` `50.0 GB`
6. Verifikasi kartu tidak memuat `10.0 GB`
7. Verifikasi kartu tidak memuat `200.0 GB`
8. Verifikasi kartu tidak memuat baris app milik Client B

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Isolasi multi-tenant (data dua Client, satu sesi login).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (precondition TC dijadikan langkah seeding), langkah 3 (membaca kartu, langkah TC). Asersi absence (langkah 6 sampai 8) didahului anchor positif nilai Client A pada langkah 4 dan 5 di kartu yang sama (bagian 8b butir 2).
- Langkah 6 sampai 8 dipisah per klausa karena tiga negasi atas nilai/baris yang berbeda; `10.0 GB` dan `200.0 GB` adalah nilai S6.
- Temuan untuk QA:
  - Mekanisme seeding laporan Storage Client B (S6) dan Client A (S1) tidak didefinisikan di TC (Q-4); ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa mengarang endpoint.
  - TC-281 hanya memeriksa isi kartu; tidak ada pembacaan endpoint langsung dengan sesi Client B.
