---
id: TC-AC-ACC-E2E-027-role-matrix-negatif-akses-url-detail-aktor-archived-read
title: "Role Matrix Negatif: Akses URL Detail Client oleh Aktor Archived-Read (403 per Status dan 404 Netral di Luar Scope)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-952
  - TC-AC-ACC-953
coverage:
  web: automated
---

# Role Matrix Negatif: Akses URL Detail Client oleh Aktor Archived-Read (403 per Status dan 404 Netral di Luar Scope)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-08 | Archived-Read (Manage archived client: Read, exact-match Area Jakarta) | `archivedReadJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ARCHIVED_READ_PASSWORD` |

- Login di hook `before` spec ini (Archived-Read, A-08); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Fixture A3 residen `C-ROL-6` `PT Arsip Menteng` (Archived, Direct, Group `Cabang Menteng`, di luar assignment exact-match Area Jakarta) hanya dibaca. Pre-setup `C-01`, `C-03`, `C-04` hanya dibaca.
- ID Client untuk URL Detail (UUID opaque) `PT Sejahtera Abadi` (C-01; Active), `PT Wahana Nusantara` (C-03; Suspended), dan `PT Arsip Menteng` (C-ROL-6; Archived) diambil dari keluaran skrip seed atau respons API; kemampuan membaca ID disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-952: Akses langsung URL Detail Client Active dan Suspended dalam scope oleh aktor Manage archived client saja: 403 per status

1. Ketik Search `PT Karya Abadi`, tekan Enter
2. Klik Company Name `PT Karya Abadi` untuk membuka Detail
3. Verifikasi Detail `PT Karya Abadi` terbuka
4. Buka URL Detail dengan ID Client `PT Sejahtera Abadi` (Active, Group `Area Jakarta`) langsung
5. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
6. Verifikasi tidak ada toast error
7. Verifikasi data Client `PT Sejahtera Abadi` tidak tampil
8. Buka URL Detail dengan ID Client `PT Wahana Nusantara` (Suspended, Group `Area Jakarta`) langsung
9. Verifikasi halaman no-access tampil (tanpa redirect ke halaman lain yang bukan no-access)
10. Verifikasi tidak ada toast error
11. Verifikasi data Client `PT Wahana Nusantara` tidak tampil

### TC-AC-ACC-953: Aktor Manage archived client berhak membuka Detail Client Archived di luar scope group: 404 netral

12. Buka Admin Console > Client lewat item `Client` pada sidebar
13. Ketik Search `PT Karya Abadi`, tekan Enter
14. Klik Company Name `PT Karya Abadi` untuk membuka Detail
15. Verifikasi Detail `PT Karya Abadi` terbuka
16. Buka URL Detail dengan ID Client `PT Arsip Menteng` (Archived) langsung
17. Verifikasi toast netral `This client is no longer available.`
18. Verifikasi halaman kembali ke List
19. Verifikasi data Client `PT Arsip Menteng` tidak tampil dan tidak ada petunjuk bahwa Client berada di luar scope

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 12. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Penyimpangan urutan (S-05): tidak ada; urutan TC sumber 952, 953 dipertahankan.
- Keputusan pemilik (klik, 2026-11-02): spec mengikuti `docs/spec-decisions.md` D-015 (menggantikan pilihan Q1 sebelumnya). Akses URL langsung tanpa capability diarahkan ke halaman no-access, tanpa toast `You don't have permission to do this.`, berlaku app-wide. Teks atau elemen pasti halaman no-access belum tercatat (spec Brand TC-GS-BRAND-E2E-010 dan D-015 hanya menyebut "halaman no-access tampil"); spec mengasersi dengan cara yang sama: halaman no-access tampil sebagai anchor positif, lalu tidak ada toast dan tidak ada data Client termuat. Toast untuk aksi atau request yang ditolak di halaman yang boleh dibuka tidak berubah. Langkah "Tunggu toast lama hilang otomatis" setelah blok no-access dihapus karena tidak ada toast.
- Pembagian TC lintas spec: akses URL Detail aktor Active-Read (TC-AC-ACC-951, 954, 965, 61, 564, 565) di spec 026.
- Temuan untuk QA:
  - Sudah selaras (2026-11-03, temuan T-1 e2e-audit): Expected TC-AC-ACC-952 dan PRD client §9.3 (butir 1 dan 3, EC-80, EC-88) kini menyebut halaman no-access tampil tanpa toast error untuk akses URL langsung tanpa capability, sama dengan D-015. Spec mengasersi halaman no-access tampil tanpa toast dan tanpa data Client. Teks atau elemen halaman no-access belum diketahui; script memakai asersi yang sama dengan spec Brand.
