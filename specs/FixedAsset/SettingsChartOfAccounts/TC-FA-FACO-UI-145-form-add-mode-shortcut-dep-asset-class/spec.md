---
id: TC-FA-FACO-UI-145-form-add-mode-shortcut-dep-asset-class
title: "Form Add Account dari shortcut konsumen: Account Function terkunci dan tanpa checkbox Stay"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FACO-LOGIC-10f
  - FACO-LOGIC-12b
  - FACO-LOGIC-12c
  - §[F-FACO-01] Create Account#r5
  - §9.4.2#r38
smoke: []
dependsOn:
  - "Asset Class: Select akun dengan shortcut `+ Create account`"
trace:
  FACO-LOGIC-10f: [9, 10]
  FACO-LOGIC-12b: [4, 5]
  FACO-LOGIC-12c: 6
  §[F-FACO-01] Create Account#r5: [9, 10]
  §9.4.2#r38: [9, 10]
anchor: [3]
coverage:
  web: automated
---

# Form Add Account dari shortcut konsumen: Account Function terkunci dan tanpa checkbox Stay

## Prerequisites
- Aktor: Total Control.
- Layar awal: Select akun pada form modul konsumen Asset Class.
- Komponen: Modal Add Account
- Data:
  - DU-145-1: Select akun konsumen yang menentukan Account Function `Asset Cost`.
- Kondisi:
  - K1: batas jumlah akun belum tercapai dan Select akun DU-145-1 menyediakan shortcut `+ Create account`
  - K2: Select akun DU-145-1 ditampilkan dengan shortcut `+ Create account`, modal Add Account belum dibuka, dan respons daftar akun membawa jumlah akun yang sama dengan ceiling batas jumlah akun

## Test Steps

### Shortcut membuka modal Add Account dengan Account Function terkunci dan tanpa checkbox Stay
1. Tampilkan Modal Add Account dengan kondisi K1
2. Klik shortcut `+ Create account` pada Select akun
3. Verifikasi tombol `[Submit]` tampil pada modal Add Account
4. Verifikasi field Account Function berisi `Asset Cost`
5. Verifikasi field Account Function Disabled
6. Verifikasi checkbox `Stay on this form after submitting` tidak tampil

### Shortcut saat batas jumlah akun tercapai menampilkan dialog blok
7. Tampilkan Select akun DU-145-1 beserta shortcut `+ Create account` dengan kondisi K2
8. Klik shortcut `+ Create account` pada Select akun
9. Verifikasi dialog berjudul `Cannot Add Account` tampil
10. Verifikasi modal Add Account tidak dibuka
