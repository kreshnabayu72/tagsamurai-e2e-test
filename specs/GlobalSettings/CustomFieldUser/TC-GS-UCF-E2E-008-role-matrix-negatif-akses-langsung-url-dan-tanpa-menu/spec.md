---
id: TC-GS-UCF-E2E-008-role-matrix-negatif-akses-langsung-url-dan-tanpa-menu
title: "Role Matrix Negatif: Aktor Tanpa Capability Tidak Melihat Menu User dan Akses Langsung URL Tab Custom Field Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-37
  - TC-GS-UCF-38
coverage:
  web: automated
---

# Role Matrix Negatif: Aktor Tanpa Capability Tidak Melihat Menu User dan Akses Langsung URL Tab Custom Field Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata).
- Spec Role Matrix negatif satu role (bagian 3a konvensi): kasus sidebar tersembunyi dan akses langsung URL dikelompokkan sebagai spec negatif tersendiri per topik.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-GS-UCF-37, 38 | Tanpa Capability (Fajar Nugroho): bukan Total Control, Read Only, maupun pemegang Manage user and role | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Akun aktor: akun Tanpa Capability login sekali di hook `before` dengan `Spectra.env.GS_NOCAP_PASSWORD`. Password tidak ditulis di spec atau fixture. Hook `after` mengembalikan sesi ke akun Total Control default suite (`Spectra.env.GS_TC_PASSWORD`).
- Layar awal: spec ini menguji sidebar dan akses langsung URL sehingga tidak memakai pembukaan layar hook `beforeEach`; langkah 6 membuka URL tab Custom Field secara langsung.
- URL tab Custom Field (Data Uji TC-GS-UCF-38): hook `before` membuka konteks Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, `Spectra.env.GS_TC_PASSWORD`) hanya untuk membaca URL tab Custom Field lalu menutup konteks itu; akun Tanpa Capability tetap menjadi sesi aktor spec.
- Data Pre-setup: Custom Field Client A (6 field Pre-setup) sebagai data latar yang tidak boleh tampil; tidak dibuat, diubah, atau dihapus. Tidak ada Data Dinamis.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor spec ini dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: navigasi langsung ke URL (setara menempel URL ke address bar lalu Enter) tanpa melalui sidebar; pembacaan daftar menu sidebar; pengamatan toast.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-37: Aktor tanpa capability dan bukan Total Control atau Read Only tidak melihat menu User dan tab Custom Field

1. Perhatikan sidebar
2. Verifikasi sidebar tampil dengan sedikitnya satu menu yang dapat diakses akun
3. Verifikasi menu Global Settings tidak tampil di sidebar
4. Verifikasi menu `User` tidak dapat dijangkau (Global Settings > User > Custom Field tidak ditemukan di sidebar)
5. Verifikasi tab `Custom Field` dan data Custom Field tidak dapat dilihat

### TC-GS-UCF-38: Akses langsung URL tab Custom Field tanpa capability ditolak

6. Tempel URL tab Custom Field (dibaca dari sesi Total Control di hook `before`) ke address bar, tekan Enter
7. Verifikasi muncul toast error: "You don't have permission to do this."
8. Verifikasi UI di-refresh
9. Verifikasi tidak ada redirect
10. Verifikasi tidak ada baris Custom Field termuat

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Visibilitas elemen tab untuk role yang memegang capability ada di spec 007; eksekusi per capability di spec 009.
- Langkah 7 (toast) diasersi lebih dulu karena toast bersifat sementara. Langkah 10 (tidak ada baris Custom Field termuat) beranchor langkah 7 (respons penolakan server sudah diterima) dan langkah 8 (UI di-refresh).
- Langkah 2 adalah asersi tambahan (anchor permukaan) di luar Expected TC-GS-UCF-37: membuktikan sidebar sudah termuat sebelum langkah 3 dan 4 mengasersi menu tidak tampil (bagian 8b butir 2: absence item menu didahului `Verifikasi` item menu lain pada sidebar yang sama).
- Konteks Total Control di hook `before` hanya membaca URL tab Custom Field dan ditutup sebelum langkah spec berjalan; tidak ada asersi di konteks itu, sehingga bukan konteks kedua kelas c dan tidak butuh butir `P-2` (bagian 3, P-2).
- Penolakan permission mengikuti keputusan NC-18 (toast global `You don't have permission to do this.`), yang berbeda dari toast gagal baku aksi di PRD awal dan dilacak di `nc-followups.md` terhadap API/LLD; asersi mengikuti TC dan bisa gagal pada backend nyata sampai API/LLD diselaraskan.
- Temuan untuk QA:
  - TC-GS-UCF-37 tidak menyebut menu sidebar yang tetap tampil bagi akun tanpa capability; spec memakai "sedikitnya satu menu yang dapat diakses" sebagai anchor generik (langkah 2) dan keberadaan menu itu perlu dikonfirmasi QA.
  - TC-GS-UCF-37 Expected b ("tab Custom Field dan data Custom Field tidak dapat dilihat") tidak punya langkah observasi sendiri; spec mengasersinya dari ketiadaan jalur menu (langkah 4 dan 5).
  - TC-GS-UCF-38 Expected a ("UI di-refresh, tanpa redirect") tidak menyebut halaman yang tampil sesudah toast; spec hanya mengasersi UI di-refresh dan tidak ada redirect.
  - TC-GS-UCF-38 tidak menyebut cara memperoleh URL tab Custom Field; mekanisme (membuka sesi Total Control di hook `before`) disediakan tim FE.
  - TC-GS-UCF-38 menyatakan akses langsung URL menghasilkan toast 403 tanpa halaman unauthorized terpisah; Position memakai pola yang sama, tetapi apakah modul ini menampilkan halaman kosong atau tab User List sesudah toast tidak disebut.
