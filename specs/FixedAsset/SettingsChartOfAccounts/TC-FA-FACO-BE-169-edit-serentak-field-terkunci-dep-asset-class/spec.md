---
id: TC-FA-FACO-BE-169-edit-serentak-field-terkunci-dep-asset-class
title: "Dua Save Edit serentak atas akun dengan Account Function terkunci"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["§[F-FACO-02] Edit Account#r19", "§[F-FACO-02] Edit Account#r20"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  "§[F-FACO-02] Edit Account#r19": [3, 5, 9, 10]
  "§[F-FACO-02] Edit Account#r20": [4, 6, 11]
---

# Dua Save Edit serentak atas akun dengan Account Function terkunci

## Prerequisites
- Aktor: Admin A dan Admin B, keduanya Total Control dengan cakupan seluruh client.
- Data:
  - DU-169-1: Account Code `LCK-{runId}`, Account Name `Kas Terkunci Dipakai {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 1, dipakai DU-169-2.
  - DU-169-2: Asset Class `Kelas Kunci Serentak {runId}`, Status `Active`; Asset Cost `LCK-{runId}`.
  - DU-169-5: Account Code `LCL-{runId}`, Account Name `Kas Terkunci Kedua {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 1, dipakai DU-169-6.
  - DU-169-6: Asset Class `Kelas Kunci Kedua {runId}`, Status `Active`; Depreciation Expense `LCL-{runId}`.
- Kondisi:
  - Kedua akun belum pernah diekspor (Last Used in Journal kosong), sehingga Account Code dan Account Name tidak terkunci dan penyebab kunci Account Function hanya pemakaian oleh Asset Class (Used By lebih dari 0).
  - Kedua akun bukan nilai default company.

## Test Steps

### Save yang mengubah Account Function terkunci ditolak sementara Save atas Account Name tersimpan
1. Admin A mencatat jumlah entri log akun `LCK-{runId}` pada Changelog
2. Admin A mengirim Edit akun `LCK-{runId}` dengan Account Code `LCK-{runId}`, Account Name `Kas Terkunci Nama A {runId}`, Account Function `Accumulated Depreciation`, dan Admin B secara serentak mengirim Edit akun `LCK-{runId}` dengan Account Code `LCK-{runId}`, Account Name `Kas Terkunci Dinamai Ulang {runId}`, Account Function `Asset Cost`
3. Verifikasi Edit Admin A ditolak karena Account Function akun terkunci oleh pemakaian Asset Class, tanpa menyimpan field apa pun dari Edit itu
4. Verifikasi Edit Admin B berhasil dan Account Name akun `LCK-{runId}` adalah `Kas Terkunci Dinamai Ulang {runId}`
5. Verifikasi Account Function akun `LCK-{runId}` tetap `Asset Cost`
6. Verifikasi Changelog memuat tepat satu entri baru untuk akun `LCK-{runId}`, yaitu Action `Edit` untuk field Account Name dengan Old Value `Kas Terkunci Dipakai {runId}` dan New Value `Kas Terkunci Dinamai Ulang {runId}`, dan tidak memuat entri baru untuk field Account Function

### Dua Save serentak yang sama-sama mengubah Account Function terkunci ditolak keduanya
7. Admin A mencatat jumlah entri log akun `LCL-{runId}` pada Changelog
8. Admin A mengirim Edit akun `LCL-{runId}` dengan Account Code `LCL-{runId}`, Account Name `Kas Terkunci Kedua {runId}`, Account Function `Gain on Disposal`, dan Admin B secara serentak mengirim Edit akun `LCL-{runId}` dengan Account Code `LCL-{runId}`, Account Name `Kas Terkunci Kedua {runId}`, Account Function `Loss on Disposal`
9. Verifikasi kedua Edit ditolak karena Account Function akun terkunci oleh pemakaian Asset Class
10. Verifikasi Account Function akun `LCL-{runId}` tetap `Depreciation Expense`
11. Verifikasi jumlah entri log akun `LCL-{runId}` pada Changelog sama dengan jumlah yang dicatat sebelum kedua Edit
