---
id: TC-AC-ACC-E2E-132-defense-client-derived-request-langsung
title: "Defense-in-depth: Change Partner, Suspend, dan Delete pada Client Derived Hidden di UI dan Request Langsung Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-184
  - TC-AC-ACC-228
  - TC-AC-ACC-198
coverage:
  web: automated
---

# Defense-in-depth: Change Partner, Suspend, dan Delete pada Client Derived Hidden di UI dan Request Langsung Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Akun aktor (urutan blok = urutan akun, Step ganti akun eksplisit):
  - Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `AC_TC_PASSWORD` (TC-AC-ACC-184 dan 228). Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite.
  - Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ACTIVE_FULL_PASSWORD` (TC-AC-ACC-198).
  - Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca; semua request ditolak sehingga data tidak berubah): C-06 `PT Maju Bersama` (Active, Derived, Partner CV Mitra Sejati sendiri).
- Kemampuan teknis (kelas a): klien HTTP/Fixture BE yang mengirim request langsung ke server memakai sesi API aktor yang sedang login (disediakan tim FE/BE; sesi API tidak dihitung sebagai sesi web, dinyatakan di `suite.md`); membaca keberadaan Client lewat Fixture BE/List.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-184: Change Partner pada Client Derived Hidden dan ditolak server

1. Ketik Search `PT Maju Bersama`, tekan Enter
2. Klik `[⋯]` pada baris `PT Maju Bersama`
3. Verifikasi `Change Partner` Hidden pada menu `[⋯]`
4. Kirim request Change Partner langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Maju Bersama`
5. Verifikasi request ditolak server dengan respons 403 Forbidden

### TC-AC-ACC-228: Delete Client Derived Hidden dan ditolak server

6. Kirim request Delete langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Maju Bersama`
7. Verifikasi request ditolak server dengan respons 403 Forbidden
8. Muat ulang List dan ketik Search `PT Maju Bersama`, tekan Enter
9. Verifikasi baris `PT Maju Bersama` tetap tampil

### Blok Active-Full

10. Ganti akun: logout lalu login sebagai Active-Full A-15

#### TC-AC-ACC-198: Suspend Client Derived Hidden dan ditolak server

11. Ketik Search `PT Maju Bersama`, tekan Enter
12. Klik `[⋯]` pada baris `PT Maju Bersama`
13. Verifikasi `Suspend` Hidden pada menu `[⋯]`
14. Kirim request Suspend langsung ke server lewat klien HTTP (tanpa melalui browser) untuk `PT Maju Bersama`
15. Verifikasi request ditolak server dengan respons 403 Forbidden

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: ketiga TC adalah kelas a dengan Expected berupa respons API (403 Forbidden); tetap masuk spec FE+BE walau tumpang tindih dengan `tc-client-backend.md`. Request langsung dikirim lewat klien HTTP (Sesi API aktor, `suite.md`) tanpa melalui browser, sehingga asersi hanya kode respons dan state data (bagian 8b butir 1); tidak ada toast atau dialog yang diasersi.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 8 (muat ulang dan Search ulang sebelum membaca keberadaan Client), langkah 10 (ganti akun).
- Asersi tambahan yang dicatat (S-03): langkah 9 (baris `PT Maju Bersama` tetap tampil) tidak ada di Expected TC-AC-ACC-228 dan ditambahkan sebagai asersi state data atas penolakan request langsung, diamati lewat List; hasil Search yang menemukan baris adalah anchor positif.
- Post Condition TC-AC-ACC-184, 228, 198: `-`.
- Temuan untuk QA:
  - TC-AC-ACC-228 tidak menyebut Client Derived yang dipakai; spec memakai C-06 dan mengasersi penolakan 403 serta keberadaan Client.
