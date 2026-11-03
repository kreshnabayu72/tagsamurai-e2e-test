---
id: TC-AC-ACC-E2E-036-defense-injeksi-script-pada-address-client-disanitasi
title: "Defense-in-depth: Input Script pada Address Client Disanitasi dan Tampil sebagai Teks Literal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-452
coverage:
  web: automated
---

# Defense-in-depth: Input Script pada Address Client Disanitasi dan Tampil sebagai Teks Literal

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-15 | Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng) | `activeFullJakarta_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` |

- Login di hook `before` spec ini (Active-Full, A-15); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Client baru dibuat spec lewat form Create: Company Name `PT Uji Xss {runId}-036`, Address `<script>alert(1)</script>`; field wajib lain diisi sesuai Data valid Create di bawah (TC tidak menyebut field wajib; lihat Temuan untuk QA). Client dibersihkan di hook `after` lewat Fixture BE.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10` (di spec ini diganti `<script>alert(1)</script>`); Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-036@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong. Company Name `PT Uji Xss {runId}-036`.
- Kemampuan teknis: mendeteksi eksekusi script (dialog `alert` browser tidak muncul) lewat penanganan dialog browser.
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-452: Input XSS pada Address disanitasi

1. Klik `[+ New Client]`
2. Isi field wajib sesuai Data valid Create, isi Company Name `PT Uji Xss {runId}-036` dan Address `<script>alert(1)</script>`, lalu klik `[Submit]`
3. Tunggu aksi `[Submit]` selesai (popup Create tertutup)
4. Ketik Search `PT Uji Xss {runId}-036`, tekan Enter
5. Lihat List
6. Verifikasi baris `PT Uji Xss {runId}-036` tampil di List
7. Verifikasi tidak ada dialog `alert` atau eksekusi script pada List
8. Klik Company Name `PT Uji Xss {runId}-036` untuk membuka Detail
9. Lihat Address pada Detail
10. Verifikasi Address tampil sebagai teks literal `<script>alert(1)</script>`
11. Verifikasi tidak ada dialog `alert` atau eksekusi script pada Detail
12. Kembali ke List dengan tombol Back browser dan klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 3, 12. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- K-1 tidak berlaku: Expected berupa tampilan literal di UI, bukan respons API.
- Penyimpangan (S-03): List tidak punya kolom Address; Address diamati di Detail, dan List diamati untuk baris Client serta tidak adanya eksekusi script.
- Temuan untuk QA:
  - TC-AC-ACC-452: judul menyebut "Company Name dan Address", tetapi langkah dan Data Uji hanya memuat Address (`<script>`); spec hanya mengisi Address dengan nilai itu. Langkah 1 ("Buat Client") tidak menyebut field wajib; nilai valid mengikuti Data valid Create di Prerequisites.
  - TC-AC-ACC-452: Expected "tidak ada eksekusi script" tidak menyebut cara mengamati; spec memakai penanganan dialog browser (tidak ada dialog `alert`).
  - TC-AC-ACC-452: Address tidak termasuk kolom List default maupun Curated (Tabel kolom §4.1.1); "Lihat List/Detail" diamati di Detail.
