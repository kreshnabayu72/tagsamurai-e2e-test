---
id: TC-GS-POS-E2E-008-role-matrix-negatif-akses-langsung-url
title: "Role Matrix Negatif: Akses Langsung URL Tab Position oleh Aktor Tanpa Capability"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-36
coverage:
  web: automated
---

# Role Matrix Negatif: Akses Langsung URL Tab Position oleh Aktor Tanpa Capability

## Prerequisites

- Mode: FE+BE (backend nyata).
- Spec Role Matrix negatif satu role (bagian 3a konvensi): kasus akses langsung URL dikelompokkan sebagai spec negatif tersendiri per topik.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-GS-POS-36 | System Role tanpa capability "Manage user and role" | `noCapabilityGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 8) | `Spectra.env.GS_NOCAP_PASSWORD` |

- Akun aktor: akun tanpa capability login sekali di hook `before` dengan `Spectra.env.GS_NOCAP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: spec ini menguji akses langsung URL sehingga tidak memakai pembukaan layar hook `beforeEach`; langkah 1 membuka URL tab Position secara langsung.
- URL tab Position (precondition "URL diketahui dari sesi Total Control"): hook `before` membuka konteks Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1, `Spectra.env.GS_TC_PASSWORD`) hanya untuk membaca URL tab Position lalu menutup konteks itu; akun tanpa capability tetap menjadi sesi aktor spec.
- Data Pre-setup: Position Pre-setup 10 sampai 16 (tanpa suffix) sebagai data latar yang tidak boleh tampil; tidak ada yang dibuat, diubah, atau dihapus. Tidak ada Data Dinamis.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` true, lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): tutup konteks Total Control bila masih terbuka, dan kembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Kemampuan teknis: navigasi langsung ke URL (setara menempel URL ke address bar lalu Enter) tanpa melalui sidebar; pengamatan toast.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### TC-GS-POS-36: Akses langsung URL tab Position oleh aktor tanpa capability

1. Tempel URL tab Position (dibaca dari sesi Total Control di hook `before`) ke address bar, tekan Enter
2. Verifikasi muncul toast error: "You don't have permission to do this."
3. Verifikasi tidak terjadi redirect ke halaman unauthorized terpisah
4. Verifikasi data tabel Position tidak ditampilkan
5. Verifikasi elemen Position yang tidak berhak (Table Tools, `[+ Position]`, kolom Checkbox, row action) tetap tersembunyi

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Visibilitas sub-tab Position untuk akun tanpa capability lewat navigasi UI diasersi di spec 007 (TC-GS-POS-25).
- Langkah 2 (toast) diasersi lebih dulu karena toast bersifat sementara.
- Konteks Total Control di hook `before` hanya membaca URL tab Position dan ditutup sebelum langkah spec berjalan; tidak ada asersi di konteks itu, sehingga bukan konteks kedua kelas c dan tidak butuh butir `P-2` (bagian 3, P-2).
- Temuan untuk QA:
  - TC-GS-POS-36 Expected b ("tidak terjadi redirect ke halaman unauthorized terpisah") tidak menyebut halaman yang tampil setelah toast; spec hanya mengasersi bahwa halaman unauthorized terpisah tidak tampil.
  - TC-GS-POS-36 precondition b ("URL tab Position diketahui dari sesi Total Control") tidak menyebut cara membaca URL; mekanismenya (membuka sesi Total Control di hook `before`) disediakan tim FE.
  - Seluruh asersi dilakukan lewat browser (navigasi URL); TC tidak memuat request langsung ke server sehingga tidak ada asersi respons HTTP.
