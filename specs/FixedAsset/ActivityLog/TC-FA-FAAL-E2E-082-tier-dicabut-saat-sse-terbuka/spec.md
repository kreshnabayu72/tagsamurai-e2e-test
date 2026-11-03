---
id: TC-FA-FAAL-E2E-082-tier-dicabut-saat-sse-terbuka
title: "Perubahan Tier Akses: Tier Dicabut saat SSE Terbuka Menutup Koneksi dan Menghentikan Event"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-272
coverage:
  web: automated
---

# Perubahan Tier Akses: Tier Dicabut saat SSE Terbuka Menutup Koneksi dan Menghentikan Event

## Prerequisites

- Mode: FE+BE.
- Akun yang dipakai:

  | Peran dalam spec | Pre-setup | Email | Env var password |
  |---|---|---|---|
  | User target pencabutan tier (Read Only), sesi UI | #9 | `readOnlyRevokeTarget_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_REVOKE_PASSWORD` |
  | Admin Total Control lain (Admin Alpha), sesi API | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
- Login akun aktor (user target #9) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Hook `after` memulihkan tier akses #9 (Read Only) dan nama group `Gedung C`, lalu mengembalikan sesi UI ke akun default suite (Total Control, Pre-setup #1).
- Sesi API aktor (butir "Sesi API aktor" di `suite.md`): admin Alpha (#1) mencabut dan meng-assign tingkat akses serta mengubah nama group lewat sesi API yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE.
- Env var `FA_RO_REVOKE_PASSWORD` dan `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (R-07). Password tidak ditulis di spec atau fixture.
- Data: Tab User Action UA-01 sampai UA-15 (Pre-setup #12, total 15 baris), dipulihkan ke keadaan Pre-setup sebelum spec (disediakan tim FE/BE). Group `Gedung C` (Dinamis #6) diubah menjadi `Gedung C1` lalu `Gedung C2` dan dipulihkan ke `Gedung C`.
- State global yang diubah spec: tier akses user #9 dan nama group `Gedung C`. Pemulihan lewat langkah penghubung di akhir spec dan hook `after`.
- Kemampuan teknis disediakan tim FE: pengamat koneksi SSE pada sesi UI target (butir "Kemampuan teknis tambahan" di `suite.md`); baseline jumlah entri Tab User Action dibaca lewat Showing teks pagination sebelum aksi.
- Jendela asersi absence SSE: 5 detik tanpa memuat ulang halaman adalah pilihan spec (bagian 6), bukan nilai TC atau PRD.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun #9.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nilai data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-272: Tier dicabut saat SSE terbuka menutup koneksi dan menghentikan event

1. Klik tab User Action
2. Catat baseline jumlah entri Tab User Action dari teks pagination
3. Pada sesi API admin Total Control (#1), ubah nama group `Gedung C` menjadi `Gedung C1` hingga tersimpan
4. Verifikasi user target: baris baru diterima otomatis tanpa memuat ulang halaman (jumlah entri bertambah satu dari baseline)
5. Pada sesi API admin Total Control (#1), cabut tingkat akses Read Only user target (#9) hingga tersimpan
6. Pada sesi API admin Total Control (#1), ubah nama group `Gedung C1` menjadi `Gedung C2` hingga tersimpan
7. Tunggu 5 detik tanpa memuat ulang halaman
8. Verifikasi user target: server menutup koneksi SSE seketika
9. Verifikasi user target: baris dari aksi sebelum pencabutan (`Gedung C1`) masih tampil di tabel
10. Verifikasi user target: baris dari aksi berikutnya (`Gedung C2`) tidak diterima dan jumlah entri tetap baseline ditambah satu
11. Pada sesi API admin Total Control (#1), ubah nama group `Gedung C2` menjadi `Gedung C` dan assign kembali tingkat akses Read Only ke user target (#9) hingga tersimpan

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pelaku kedua (admin Total Control lain) memakai sesi API; bukan konteks kedua kelas c (bagian 3 prinsip 13, P-2 keputusan 2026-10-30), jadi tidak memakai butir `P-2`. Sesi UI hanya satu dan akunnya login di hook `before` (S-07).
- Langkah penghubung (S-03): langkah 1 dan 2 (tab User Action dan baseline, S-12), langkah 11 (pemulihan nama group dan tier lewat sesi API).
- Langkah 3, 5, 6, dan 11 memicu perubahan state lewat sesi API dan ditulis "... hingga ... tersimpan" (R-20).
- Langkah 10 (absence) didahului anchor positif langkah 9 (baris aksi sebelum pencabutan yang masih tampil di tabel yang sama) dan jendela 5 detik langkah 7 (bagian 6).
- Temuan untuk QA:
  - TC-FA-FAAL-272 tidak menyebut env var password; nama env var diusulkan dari butir "Env var" di `suite.md`.
  - TC-FA-FAAL-272 tidak menyebut cara mengamati penutupan koneksi SSE; spec memakai pengamat koneksi SSE yang disediakan tim FE tanpa mengarang mekanisme.
  - TC-FA-FAAL-272 Post Condition tidak ada; pemulihan di langkah 11 adalah langkah penghubung spec.
