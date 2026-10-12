---
id: TC-GS-BRAND-E2E-075-log-absence-dua-sesi-dan-request-langsung
title: "Tidak Ada Entri Log Kedua untuk Delete Record yang Sudah Terhapus dan Tidak Ada Entri Delete untuk Request Langsung ke Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-213
  - TC-GS-BRAND-227
coverage:
  web: automated
---

# Tidak Ada Entri Log Kedua untuk Delete Record yang Sudah Terhapus dan Tidak Ada Entri Delete untuk Request Langsung ke Server

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Sesi pertama (UI) | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Admin kedua (hanya lewat API, tanpa login UI) | Total Control Client A (admin kedua, Nadia Pratama) | `totalControlSecond_automated_qaTeam1@qwertysystem.net` | `GS_TC2_PASSWORD` |

  Login sesi pertama di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Akun admin kedua adalah fixture baru (Tabel Data Uji Pre-setup) yang disediakan tim FE; ia berbeda dari akun sesi pertama.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (`GS_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak diubah spec ini, tanpa suffix `{runId}`): `Acme Corp` (in-use: FAMS Asset Name Forklift); request Delete ke server ditolak sehingga brand ini tidak berubah.
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi): `Gale Co {runId}-075` (D-19), brand bebas relasi, di-seed lewat API di hook `before` oleh akun sesi pertama dan dihapus oleh admin kedua pada TC-GS-BRAND-213 (setara dependensi TC-GS-BRAND-103).
- Kemampuan teknis: (a) sesi API atas akun admin kedua (login lewat API dengan `Spectra.env.GS_TC2_PASSWORD`) untuk menghapus brand tanpa melewati UI sesi pertama; (b) mengirim request HTTP langsung ke server dengan token sesi Total Control Client A (sesi pertama) tanpa melewati dialog UI.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Gale Co {runId}-075` bila masih ada.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-213: login sebagai Total Control; Gale Co (D-19) dan admin kedua siap. TC-GS-BRAND-227: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-227: Server menolak Delete Brand in-use walau dialog dilewati (Expected Result b)

1. Kirim request Delete Acme Corp langsung ke server (tanpa melewati dialog) dengan sesi pertama
2. Buka Changelog Brand, filter Action `Delete`, lalu Search `Acme Corp`
3. Verifikasi tidak ada entri Delete Acme Corp di Changelog

### TC-GS-BRAND-213: Delete record yang sudah terhapus tidak membuat entri kedua

4. Tutup Changelog, Search `Gale Co {runId}-075` pada tabel Brand, pastikan baris `Gale Co {runId}-075` tampil
5. Klik `⋯` pada baris `Gale Co {runId}-075` > Delete → dialog `Delete Brand` tampil
6. Admin kedua (akun `totalControlSecond_automated_qaTeam1@qwertysystem.net`, lewat API) menghapus `Gale Co {runId}-075`
7. Pada sesi pertama, klik [Delete] pada dialog
8. Buka Changelog, Search `Gale Co {runId}-075`
9. Verifikasi Changelog hanya memuat satu entri Delete Gale Co (dari admin kedua)
10. Buka Global Settings > Activity Log, Search `Gale Co {runId}-075`
11. Verifikasi Activity Log juga hanya memuat satu entri Delete Gale Co

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Spec ini kelas g (asersi absence) yang memuat dua harness ringan: admin kedua lewat API (TC-GS-BRAND-213) dan request HTTP langsung ke server (TC-GS-BRAND-227). Keduanya tidak memakai browser kedua.
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-BRAND-227 lebih dulu karena tidak menghapus data, lalu TC-GS-BRAND-213 yang menghapus data milik spec sendiri.
- TC-GS-BRAND-227 masuk `sourceTc` hanya untuk Expected Result b ("Tidak ada entri Delete di Changelog"). Expected Result a (Acme Corp tetap ada) ada di spec `TC-GS-BRAND-E2E-068-defense-in-depth-bypass-server-dan-xss`. Request Delete Acme Corp langsung ke server karenanya dikirim sekali di spec 068 dan sekali di spec ini (langkah 1), karena asersi absence dipisah dari asersi fungsional.
- Dependensi TC-GS-BRAND-103 dijalankan sebagai langkah 5 sampai 7 dengan urutan sesuai TC (dialog dibuka dulu, admin kedua menghapus, baru klik [Delete]). Expected Result TC-GS-BRAND-103 a dan b (respons `404`, toast "This brand is no longer available.", list di-refresh) diverifikasi di spec `TC-GS-BRAND-E2E-026-konflik-delete-dua-admin`; TC-GS-BRAND-213 hanya mengasersi entri log.
- Langkah penghubung: langkah 2 (Search `Acme Corp` bersama filter Delete supaya asersi absence dibatasi pada Acme Corp), langkah 4 (menutup Changelog dan mencari baris Gale Co di tabel Brand sebelum membuka menu aksinya).
