---
id: TC-GS-USER-E2E-022-create-user-happy-path-single-dan-stay-on-form
title: "Create User: Happy path pembuatan single user dan multiple user via Stay on form"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-117
  - TC-GS-USER-128
  - TC-GS-USER-129
  - TC-GS-USER-130
  - TC-GS-USER-131
  - TC-GS-USER-132
  - TC-GS-USER-133
  - TC-GS-USER-134
  - TC-GS-USER-135
  - TC-GS-USER-136
  - TC-GS-USER-137
  - TC-GS-USER-138
  - TC-GS-USER-1008
coverage:
  web: automated
---

# Create User: Happy path pembuatan single user dan multiple user via Stay on form

## Prerequisites

- Login sebagai Role: Total Control
- Dropdown Position dan Division tersedia

## Test Steps

### Pembuatan User Tunggal

1. Buka modal '[+ User]'
2. Isi First Name 'Budi', Last Name 'Santoso', Email unik, Position 'Staff', Division 'General Affairs', Access 'Fixed Asset'
3. Klik tombol '[Submit]'
4. Verifikasi toast sukses 'User created successfully.' tampil dan modal tertutup
5. Verifikasi baris Budi Santoso muncul di User List dengan status Pending Activation

### Pembuatan Multiple User via Stay on Form

6. Buka kembali modal '[+ User]', centang checkbox 'Stay on this form after submitting'
7. Isi data user Andre Kurniawan, klik '[Submit]'
8. Verifikasi toast sukses muncul, form tetap terbuka, dan input form ter-reset bersih dengan checkbox Stay tetap tercentang
9. Isi data user Maya Anggraini, klik '[Submit]', lalu uncheck Stay dan submit user Rudi Hakim
10. Verifikasi modal otomatis tertutup setelah Rudi Hakim dibuat dan ketiga user tampil di User List

## Notes

- Menggabungkan 13 test case granular (TC-GS-USER-117 s.d. TC-GS-USER-1008).
