---
id: TC-GS-GSET-E2E-046-multi-konteks-isolasi-dua-tenant
title: "Dua tenant"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-121
  - TC-GS-GSET-144
coverage:
  web: automated
---

# Dua tenant

## Prerequisites

- Mode: FE+BE.
- Akun Client A: Total Control, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No 1, staf `Client A`), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.
- Akun Client Lain: Total Control staf `Client Lain` (Tabel Data Uji Pre-setup No 18). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, kredensial `Spectra.env.GS_CLIENTLAIN_TC_PASSWORD` (nama env baru).
- Environment variable: `GS_TC_PASSWORD` dan `GS_CLIENTLAIN_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `GS_CLIENTLAIN_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan pada tahap script).
- Dua tenant (kelas multi-konteks): konteks Client A dan konteks Client Lain berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` spec ini (seedSession, kredensial dari env var). Konteks Client A membuka Global Settings > General Settings di hook `beforeEach`; konteks Client Lain membukanya pada langkah 3. Langkah ditandai `[Client A]` dan `[Client Lain]`. Hook `after` menutup konteks Client Lain dan mengembalikan sesi ke akun default suite.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` untuk kedua akun dan pemulihan record Client A ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri.
- Data: record Client A pada baseline Pre-setup No 10 (`IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Record `Client Lain` memakai Currency Code `USD` (precondition TC-GS-GSET-144), disetel oleh sesi API staf Client Lain di hook `before` bila belum; nilai Currency Code dan Date Format awal Client Lain dicatat di hook `before` dan dipulihkan di hook `after`. Date Format awal Client Lain dibaca dari form pada langkah 3 dan dicatat sebagai `{dfLain}`. Nilai yang disimpan spec: Client A Date Format `M/d/yy` (TC-GS-GSET-121); Client Lain tidak disimpan.
- Kemampuan teknis: (a) dua konteks browser paralel dengan akun dari tenant berbeda; (b) sesi API Total Control Client A dan staf Client Lain untuk PUT `/v2/enterprise-management/general-settings` (`API/openapi.yaml`; klien HTTP dan penangkapan token disediakan tim FE); (c) membaca pesan SSE yang diterima halaman konteks Client Lain sejak langkah 3 (mekanisme dan endpoint disediakan tim FE, tidak dikarang); (d) jeda nyata 5 detik pada langkah 7 sebagai jendela bagi event SSE (durasi dipilih spec sebagai jendela amat; TC tidak menyebut durasi).
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- State global yang diubah: Date Format record Client A, dipulihkan oleh hook `beforeEach` dan `after` suite. Record Client Lain dikembalikan ke nilai awalnya di hook `after`. Entri Changelog bersifat audit trail permanen dan tidak dihapus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-144: Pembacaan General Settings hanya memuat record entitas aktor (isolasi entitas)

1. [Client A] Verifikasi Select Currency Code menampilkan nilai `Client A` (`IDR`, label `Rp - Indonesian Rupiah`)
2. [Client A] Verifikasi Select Currency Code tidak menampilkan nilai `Client Lain` (`USD`)

### TC-GS-GSET-121: Event SSE hanya diterima entitas yang sama (isolasi tenant)

3. [Client Lain] Buka Global Settings > General Settings, catat Date Format yang tampil sebagai `{dfLain}`, lalu mulai merekam pesan SSE yang diterima halaman
4. [Client A] Pilih Date Format `M/d/yy`
5. [Client A] Klik `[Save]`
6. [Client A] Verifikasi toast sukses `Success, general settings has been saved.`
7. [Client Lain] Tunggu 5 detik tanpa memuat ulang halaman
8. [Client Lain] Verifikasi Select Date Format tetap `{dfLain}` (format `Client Lain` tidak berubah)
9. [Client Lain] Verifikasi halaman tidak menerima event SSE sejak langkah 3

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-121 dan TC-GS-GSET-144). Mode: FE+BE. Kelas: multi-konteks (dua tenant, prinsip 13 butir c).
- Urutan TC dibalik dari nomor TC (TC-GS-GSET-144 lebih dulu): TC-GS-GSET-144 hanya membaca (screening), TC-GS-GSET-121 mengubah state (Save), sehingga bagian baca tidak terpengaruh perubahan Client A (prinsip 13, urutan screening dulu).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 (membuka halaman dan mencatat nilai awal) dan langkah 7 (jeda). Konteks diganti secara eksplisit lewat penanda `[Client A]` dan `[Client Lain]`.
- Langkah 6 adalah `Verifikasi` tambahan di luar Expected TC sebagai anchor positif untuk asersi tidak berubah pada langkah 8 dan 9 (bagian 8b butir 2): Save Client A benar-benar berhasil.
- Dependensi TC-GS-GSET-121 dan TC-GS-GSET-144 adalah "-" pada TC.
- Temuan untuk QA:
  - Akun staf `Client Lain` tidak tertulis di Tabel Data Uji Pre-setup (No 18 hanya menyebut entitasnya). Spec menuliskannya "disediakan tim FE".
  - TC-GS-GSET-121 Expected "tidak menerima event" tidak menyebut cara mengamati event. Spec mengasersi tidak ada perubahan tampilan (langkah 8) dan tidak ada pesan SSE yang diterima (langkah 9) dengan kemampuan pembacaan pesan SSE yang disediakan tim FE.
  - TC-GS-GSET-121 Expected absence ("Tab 2 tidak berubah (format `Client Lain` tetap) dan tidak menerima event") tidak menyebut jendela amat atau durasi tunggu; spec menambah jeda 5 detik tanpa memuat ulang halaman (langkah 7) sebelum asersi absence.
  - TC-GS-GSET-121 Date Format awal `Client Lain` tidak disebut ("format `Client Lain` tetap"); spec membaca nilainya saat runtime.
