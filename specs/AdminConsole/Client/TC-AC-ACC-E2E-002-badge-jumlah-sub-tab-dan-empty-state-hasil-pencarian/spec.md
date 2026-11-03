---
id: TC-AC-ACC-E2E-002-badge-jumlah-sub-tab-dan-empty-state-hasil-pencarian
title: "Badge Jumlah Sub-tab dan Empty State Hasil Pencarian List Client"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-5
  - TC-AC-ACC-6
  - TC-AC-ACC-23
  - TC-AC-ACC-24
coverage:
  web: automated
---

# Badge Jumlah Sub-tab dan Empty State Hasil Pencarian List Client

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Mode tidak memakai intercept atau jam server. Spec read-only; state Search, Filter, dan pilihan node Group dipulihkan dalam spec (langkah penghubung).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-5: Badge jumlah Client per sub-tab tidak terpengaruh Search dan Filter Panel

1. Catat badge jumlah pada sub-tab `Active`, `Suspended`, `Archived` dan jumlah total baris tabel `Active` (baseline)
2. Ketik Search `Sejahtera`, tekan Enter
3. Verifikasi jumlah baris tabel `Active` berbeda dari baseline
4. Buka Filter Panel, pilih field `Partner` dengan `CV Mitra Lestari`, klik `[Apply]`
5. Verifikasi jumlah baris tabel `Active` mengikuti Search dan Filter (berbeda dari baseline)
6. Verifikasi badge jumlah pada ketiga sub-tab sama dengan baseline
7. Klik `[Clear Field]` pada field `Partner`, klik `[Apply]`, lalu klik `(←)` pada kotak Search

### TC-AC-ACC-6: Badge jumlah per sub-tab mengikuti pilihan node Sidebar Group Tree

8. Catat badge ketiga sub-tab dengan `[All Groups]` terpilih (baseline)
9. Klik node `Area Surabaya` pada Sidebar Group Tree
10. Verifikasi badge sub-tab `Active` bernilai 1 (`PT Timur Perkasa`)
11. Verifikasi badge sub-tab `Suspended` bernilai 0 dan `Archived` bernilai 0, dihitung ulang hanya untuk Client pada Group yang dipilih
12. Klik `[All Groups]`

### TC-AC-ACC-23: Empty state hasil Search kosong

13. Catat badge jumlah ketiga sub-tab dan jumlah total baris tabel `Active` (baseline)
14. Ketik Search `zzzzzz`, tekan Enter
15. Verifikasi empty state: ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
16. Verifikasi badge jumlah ketiga sub-tab tidak berubah dari baseline

### TC-AC-ACC-24: Pulih dari empty state dengan menghapus Search

17. Kosongkan isi kotak Search, tekan Enter
18. Verifikasi empty state hilang
19. Verifikasi tabel kembali menampilkan seluruh Client sub-tab `Active` (jumlah total baris sama dengan baseline TC-AC-ACC-23)

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 7, 12. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- Pembagian TC lintas spec: screening List dan row states ada di spec 001; isi sel di spec 003 dan 004.
- Langkah 1 TC-AC-ACC-24 (Ketik Search `zzzzzz`, tekan Enter) dipenuhi oleh state akhir TC-AC-ACC-23 yang memakai query identik, sesuai aturan halaman yang sama dipakai berulang (bagian 3, prinsip 13).
- Hitungan mutlak hanya untuk node Area Surabaya (Active 1, Suspended 0, Archived 0, populasi tertutup Tabel A3); badge lain diasersi relatif terhadap baseline.
- Temuan untuk QA:
  - TC-AC-ACC-5: Expected butir a ("jumlah baris tabel berubah mengikuti search/filter") tidak menyebut jumlah pasti; spec mengasersi relatif terhadap baseline yang dicatat. Hasil gabungan Search `Sejahtera` dan Filter Partner `CV Mitra Lestari` bisa kosong (PT Sejahtera Abadi berelasi CV Mitra Sejati); spec tidak menebak bentuk hasilnya.
  - TC-AC-ACC-6: Expected hanya menyebut Active = 1; nilai Suspended 0 dan Archived 0 diturunkan dari tabel populasi node Area Surabaya pada Tabel A3.
