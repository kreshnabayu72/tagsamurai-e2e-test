---
id: TC-GS-USER-E2E-073-user-detail-header-general-information
title: 'Header dan General Information User Detail, termasuk tampilan Custom Fields'
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-382
  - TC-GS-USER-383
  - TC-GS-USER-384
  - TC-GS-USER-385
  - TC-GS-USER-386
  - TC-GS-USER-536
coverage:
  web: automated
---

# Header dan General Information User Detail, termasuk tampilan Custom Fields

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Budi Santoso" berstatus Activated dan Active, punya Employee ID, Custom Field aktif dengan value terisi, dan Phone tersimpan `+62812345678901234`
- User "Rudi Reset" berstatus Activated dengan email pending (`pendingEmail` terisi)
- Spec ini tidak mengubah data

## Test Steps

### Header dan susunan halaman

1. Buka User Detail "Budi Santoso"
2. Verifikasi breadcrumb "User > Detail" (segmen terakhir "Detail", bukan nama user)
3. Verifikasi Header berisi Avatar dan Full Name di kiri, toggle Active di kanan atas, badge status selalu tampil di bawah nama, Employee ID sebagai subtitle, selector "Viewing: [Global Settings ▾]", dan menu `[⋯]`
4. Verifikasi Body berurutan: Section General Information, Section Custom Fields (collapsible), lalu Tab bar paling bawah dengan Role (aktif), Responsibilities, Non-Login User, Changelog, System Log, User Log
5. Klik menu `[⋯]` dan verifikasi berisi "Edit Profile" dan "Delete User" (danger) dalam satu menu

### General Information

6. Verifikasi sub-section Identity menampilkan Position, Division, dan Email, tanpa mengulang Full Name dan Photo
7. Buka User Detail "Rudi Reset" dan verifikasi di bawah field Email tampil "Pending email change to [email baru]" dan badge status "Pending Email Confirmation"

### Custom Fields

8. Kembali ke User Detail "Budi Santoso" dan expand Section Custom Fields tanpa hover atau klik
9. Verifikasi semua Custom Field aktif tampil berformat "Label: Value" dalam grid 2 kolom
10. Verifikasi field Phone tampil terformat "+62 812345678901234" (dengan spasi antara kode dan nomor)

## Notes

- Sumber `user.md` bagian 4.1, 4.2 dan `custom-field-user/PRD/custom-field-user.md` bagian 4.3.
- Teks badge Pending Email memakai "Pending Email Confirmation" sampai `GAP-279` diputuskan.
- Interaksi inline-edit Custom Field dicakup `TC-GS-USER-E2E-064-custom-field-inline-edit`. Spec ini murni tampilan.
- Aksi Header yang Disabled untuk target tertentu dicakup `TC-GS-USER-E2E-074-user-detail-header-guard-target`.
