---
id: TC-GS-PROFILE-E2E-002-screening-identity-tag-authenticator
title: "Screening halaman: Section Identity, User TAG, Authenticator, loading, dan tanpa aksi administratif"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-10
  - TC-GS-PROFILE-11
  - TC-GS-PROFILE-12
  - TC-GS-PROFILE-15
  - TC-GS-PROFILE-22
  - TC-GS-PROFILE-23
  - TC-GS-PROFILE-27
  - TC-GS-PROFILE-29
coverage:
  web: automated
---

# Screening halaman: Section Identity, User TAG, Authenticator, loading, dan tanpa aksi administratif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Pre-setup #1 Andi Pratama (`totalControlProfile_automated_{namaCompany}@qwertysystem.net`), Total Control, Position Finance Manager, Division Finance, Email `andipratama@qwertysystem.net`, TAG `TAG-0001` terpasang (plan Growth), Authenticator Enrolled; password `Spectra.env.GS_PROFILE_TC_PASSWORD`.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Kemampuan teknis: intercept jaringan di browser yang menahan respons fetch data My Profile selama 3 detik di atas backend nyata (langkah 20 sampai 27, TC-GS-PROFILE-27). Intercept hanya menahan respons untuk mengamati indikator loading; respons tidak diubah atau digagalkan. Endpoint pemuatan data My Profile mengikuti kontrak modul; spec tidak menetapkan nama endpoint.
- Data Dinamis: tidak ada. Intercept dilepas di langkah 27 dan juga di hook `after` sebagai cadangan.

## Test Steps

### Section Identity (TC-GS-PROFILE-10, TC-GS-PROFILE-11)

1. Verifikasi Position `Finance Manager` tampil di Section Identity
2. Verifikasi Division `Finance` tampil di Section Identity
3. Verifikasi Email `andipratama@qwertysystem.net` tampil di Section Identity
4. Verifikasi tidak ada kontrol ubah pada field Position, Division, dan Email
5. Hover field Email di Section Identity
6. Verifikasi tidak ada tombol Change Email, Resend Activation Email, Resend Confirmation Email, dan Cancel pending email

### Sub-section User TAG dan Authenticator (TC-GS-PROFILE-12, TC-GS-PROFILE-15)

7. Verifikasi sub-section User TAG menampilkan Badge `Verified`
8. Verifikasi TAG ID `TAG-0001` tampil pada sub-section User TAG
9. Verifikasi tidak ada tombol Scan TAG dan tombol Unpair pada sub-section User TAG
10. Verifikasi sub-section Authenticator menampilkan Badge `Enrolled` (severity success)
11. Verifikasi teks muted `Lost your device? Contact your administrator.` tampil di bawah Badge `Enrolled`
12. Verifikasi tidak ada tombol Reset Authenticator
13. Verifikasi teks petunjuk bukan tombol dan bukan tautan

### Tanpa aksi administratif dan tanpa Tab log (TC-GS-PROFILE-22, TC-GS-PROFILE-23)

14. Amati sub-section User TAG, lalu sub-section Authenticator
15. Verifikasi tidak ada Scan TAG, Unpair TAG, Reset Authenticator, Remove Access, Resend Activation Email, dan Resend Confirmation Email
16. Amati area di bawah Section Custom Field dan seluruh halaman
17. Verifikasi tidak ada Tab Role, Responsibilities, Non-Login User, Changelog, System Log, dan User Log

### Empty state tidak berlaku (TC-GS-PROFILE-29)

18. Verifikasi Header, Section Identity, Section Access & Status, dan Section Custom Field milik Andi Pratama tampil
19. Verifikasi tidak ada tampilan `No results found`

### Loading saat data dimuat pertama kali (TC-GS-PROFILE-27)

20. Pasang intercept yang menahan respons fetch data My Profile selama 3 detik
21. Klik icon Profile di navbar
22. Klik item `My Profile` di account menu
23. Verifikasi indikator loading tampil selama fetch berlangsung
24. Tunggu respons tiba
25. Verifikasi indikator loading hilang
26. Verifikasi isi halaman My Profile tampil
27. Lepas intercept

## Notes

- Sumber TC: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-10, 11, 12, 15, 22, 23, 27, 29).
- Urutan TC di spec berbeda dari urutan sumber: TC-GS-PROFILE-27 ditaruh terakhir karena memasang intercept dan membuka ulang halaman; TC-GS-PROFILE-29 dibaca sebelum itu pada halaman yang sudah termuat.
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 5, 14, dan 16 adalah aksi amati TC; langkah 20 sampai 22, 24, dan 27 memasang dan melepas intercept serta membuka ulang My Profile.
- TC-GS-PROFILE-27 memakai intercept hanya untuk menahan respons supaya indikator loading teramati. Itu bukan kegagalan yang dipaksa (kelas b), sehingga spec tetap fungsional (bagian 3 prinsip 13 butir b).
- Asersi absence pada langkah 4, 6, 9, 12, 15, 17, dan 19 didahului `Verifikasi` elemen lain pada halaman yang sama sudah tampil (langkah 1 sampai 3, 7 sampai 8, 10 sampai 11, dan 18) sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-PROFILE-27 tidak menyebut bentuk indikator loading (spinner, skeleton, atau teks); spec menulis `Verifikasi indikator loading tampil` apa adanya.
